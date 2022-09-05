"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/24 9:50
@Author  : zhangjiajun
@Github  :
@Software: PyCharm
@File    : test_PageSwitch.py
"""


import pytest
import test_CanSend
import time
global zcanlib
global chn_handle

def run_137():
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
            for i in range(8):
                msgs.frame.data[i] = int(data[i],16)
            for i in range(5):
                zcanlib.TransmitFD(chn_handle, msgs, transmit_num)
                time.sleep(2)

def test_main():
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
    run_137()
