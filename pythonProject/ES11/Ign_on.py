"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/19 13:25
@Author  : zhangjiajun
@Github  :
@Software: PyCharm
@File    : Ign_on.py
"""


import time
import threading
import test_CanSend
global zcanlib
global chn_handle
global thread1
global thread2

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
        print('aaaa')

def ign_on():
    thread1 = threading.Thread(target=run_0x295_on)
    thread2 = threading.Thread(target=run_0x501)
    thread1.start()
    thread2.start()

if __name__ == "__main__":
    ign_on()
