"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/24 9:50
@Author  : zhangjiajun
@Github  :
@Software: PyCharm
@File    : test_PageSwitch.py

功能页面切换测试
"操作步骤：
   1) 固定菜单页的切换:左右切换5次切换频率2s一次，循环操作，持续6小时
   2)固定菜单页的切换:上一页切换5次-下一页切换5次，切换频率2s一次，循环操作，持续6小时"

"""



import test_CanSend
import time
global zcanlib
global chn_handle
import threading

class Test:
    def run_0x295_on(self):
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

    def run_0x501(self):
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

    def run_0x244(self):
        while True:
            transmit_num = 1
            msgs = test_CanSend.ZCAN_TransmitFD_Data()
            for i in range(transmit_num):
                msgs.transmit_type = 0
                msgs.frame.eff = 0
                msgs.frame.rtr = 0
                msgs.frame.can_id = int('244', 16)
                msgs.frame.len = 8
                str0 = "00 40 00 00 00 00 00 00"
                str1 = "00 10 00 00 00 00 00 00"
                str2 = "00 04 00 00 00 00 00 00"
                str3 = "00 01 00 00 00 00 00 00"

                str = [str0, str1, str2, str3]
                for i in range(4):
                    data = str[i].split(' ')
                    for j in range(8):
                        msgs.frame.data[j] = int(data[j],16)
                    for k in range(5):
                        zcanlib.TransmitFD(chn_handle, msgs, transmit_num)
                        time.sleep(2)

    def run_0x2FB(self):
        transmit_num1 = 1
        msgs1 = test_CanSend.ZCAN_TransmitFD_Data()
        for i in range(transmit_num1):
            msgs1.transmit_type = 0
            msgs1.frame.eff = 0
            msgs1.frame.rtr = 0
            msgs1.frame.can_id = int('2FB', 16)
            msgs1.frame.len = 8
            str1 = "00 00 00 00 00 00 00 00"
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
    thread1 = threading.Thread(target=Test().run_0x295_on)
    thread2 = threading.Thread(target=Test().run_0x501)
    thread1.start()
    thread2.start()
    # time.sleep(30)
    thread3 = threading.Thread(target=Test().run_0x2FB)
    thread3.start()
    time.sleep(3)
    Test().run_0x244()
