"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/08/29 18:07:30
@Author  : zhangjiajun
@Github  : git@github.com:ZhangJiajun123456/ES11_automation.git
@Software: PyCharm
@File    : test_Chime.py
Chime测试
操作步骤：
  1) 录制Chime模块中车门开启指示灯报警音、前碰预警报警音、安全带未系报警音、超速报警等信号， 每隔0.5s激活一个，激活所有
  2) 持续12小时以上
"""

import time
from Common import common
import threading
import test_CanSend
global zcanlib
global chn_handle
import os
import xlrd2


vehicle = "1234567"
phone  = "3TG0221820007792"
device = common.Test(vehicle,phone)
d1 = device.d1
d2 = device.d2


def run_0x295_on():
    transmit_num1 = 1
    msgs1 = test_CanSend.ZCAN_TransmitFD_Data()
    for i in range(transmit_num1):
        msgs1.transmit_type = 0
        msgs1.frame.eff = 0
        msgs1.frame.rtr = 0
        msgs1.frame.can_id = int('295', 16)
        msgs1.frame.len = 8
        str1 = "00 A0 00 00 00 00 00 00"
        data1 = str1.split(' ')
        msgs1.frame.data[0] = int(data1[0], 16)
        msgs1.frame.data[1] = int(data1[1], 16)
        msgs1.frame.data[2] = int(data1[2], 16)
        msgs1.frame.data[3] = int(data1[3], 16)
        msgs1.frame.data[4] = int(data1[4], 16)
        msgs1.frame.data[5] = int(data1[5], 16)
        msgs1.frame.data[6] = int(data1[6], 16)
        msgs1.frame.data[7] = int(data1[7], 16)
    while True:
        zcanlib.TransmitFD(chn_handle, msgs1, transmit_num1)
        time.sleep(0.05)

def run_0x501():
    transmit_num2 = 1
    msgs2 = test_CanSend.ZCAN_TransmitFD_Data()
    for i in range(transmit_num2):
        msgs2.transmit_type = 0
        msgs2.frame.eff = 0
        msgs2.frame.rtr = 0
        msgs2.frame.can_id = int('501', 16)
        msgs2.frame.len = 8
        str2 = "00 00 00 00 00 00 00 00"
        data2 = str2.split(' ')
        msgs2.frame.data[0] = int(data2[0], 16)
        msgs2.frame.data[1] = int(data2[1], 16)
        msgs2.frame.data[2] = int(data2[2], 16)
        msgs2.frame.data[3] = int(data2[3], 16)
        msgs2.frame.data[4] = int(data2[4], 16)
        msgs2.frame.data[5] = int(data2[5], 16)
        msgs2.frame.data[6] = int(data2[6], 16)
        msgs2.frame.data[7] = int(data2[7], 16)
    while True:
        zcanlib.TransmitFD(chn_handle, msgs2, transmit_num2)

        
def test_chime():
    table = xlrd2.open_workbook('../信号梳理.xlsx')
    table = table.sheets()[0]
    #遍历canid
    canid_data = table.col_values(0, start_rowx=205, end_rowx=406)
    canmsg_data = table.col_values(3, start_rowx=205, end_rowx=406)
    for i in range(len(canid_data)):
        if type(canid_data[i]) == float:
            canid_data[i] = int(canid_data[i])

    transmit_num = 1
    msgs = test_CanSend.ZCAN_TransmitFD_Data()
    while True:
        for i in range(len(canmsg_data)):
            msgs.transmit_type = 0
            msgs.frame.eff = 0
            msgs.frame.rtr = 0
            msgs.frame.can_id = int(str(canid_data[i]), 16)
            str1 = canmsg_data[i]
            data = str1.split(' ')
            msgs.frame.len = len(data)
            #判断报文长度
            if len(data) == 8:
                for j in range(8):
                    msgs.frame.data[j] = int(data[j], 16)
            elif len(data) == 16:
                for j in range(16):
                    msgs.frame.data[j] = int(data[j], 16)
            else:
                for j in range(64):
                    msgs.frame.data[j] = int(data[j], 16)

            zcanlib.TransmitFD(chn_handle, msgs, transmit_num)
            # time.sleep(0.5)
            print(i)


if __name__ == "__main__":
    zcanlib = test_CanSend.ZCAN()
    handle = zcanlib.OpenDevice(test_CanSend.ZCAN_USBCANFD_200U, 0, 0)
    if handle == test_CanSend.INVALID_DEVICE_HANDLE:
        print("Open Device failed!")
        exit(0)
    print("device handle:%d." % (handle))

    info = zcanlib.GetDeviceInf(handle)
    print("Device Information:\n%s" % (info))
    #
    # Start CAN
    chn_handle = test_CanSend.can_start(zcanlib, handle, 0)
    print("channel handle:%d." % (chn_handle))
    thread1 = threading.Thread(target=run_0x295_on)
    thread2 = threading.Thread(target=run_0x501)
    thread1.start()
    thread2.start()
    time.sleep(30)
    test_chime()




