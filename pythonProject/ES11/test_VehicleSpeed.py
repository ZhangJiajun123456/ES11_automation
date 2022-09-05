"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/19 13:21
@Author  : starnight_cyber
@Github  : https://github.com/starnightcyber
@Software: PyCharm
@File    : test_VehicleSpeed.py
车速测试
操作步骤：
  1) 仪表车速指针从0km/h->60km/h->120km/h->180km/h->240km/h
  2) 仪表车速指针从240km/h->180km/h->120km/h->60km/h->0km/h
  3) 将上述组合再一起进行循环回放，持续12小时

"""
import os
import time
import threading
import test_CanSend
global zcanlib
global chn_handle
import test_Interaction
import test_MultimediaSwitch
import test_BtConnect

class Test:
    #抓log
    # def catch_log(self):
    #     os.system("adb -s 1234567 logcat -c")
    #     os.system("adb -s 1234567 logcat -v time > D:\Monkey\log\crash.txt")
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

    def run_137(self):
        transmit_num = 1
        msgs = test_CanSend.ZCAN_TransmitFD_Data()
        for i in range(transmit_num):
            msgs.transmit_type = 0
            msgs.frame.eff = 0
            msgs.frame.rtr = 0
            msgs.frame.can_id = int('137', 16)
            msgs.frame.len = 64
            str0 = "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 05 50 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 20 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
            str1 = "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 05 50 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 23 f5 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
            str2 = "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 05 50 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 27 fc 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
            str3 = "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 05 50 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 2c 0c 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
            str4 = "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 05 50 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 30 1c 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 "
            str = [str0,str1,str2,str3,str4]
            while True:
                for i in range(4):
                    data = str[i+1].split(' ')
                    print(data)
                    for i in range(64):
                        msgs.frame.data[i] = int(data[i], 16)
                    for i in range(30):
                        zcanlib.TransmitFD(chn_handle, msgs, transmit_num)
                        time.sleep(0.05)
                for i in range(4):
                    data = str[3 - i].split(' ')
                    print(data)
                    for i in range(64):
                        msgs.frame.data[i] = int(data[i], 16)
                    for i in range(30):
                        zcanlib.TransmitFD(chn_handle, msgs, transmit_num)
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
    time.sleep(5)
    # thread3 = threading.Thread(target=Test().catch_log)
    # thread3.start()
    thread4 = threading.Thread(target=Test().run_137)
    # thread5 = threading.Thread(target=test_MultimediaSwitch.Test().test_SwitchBetweenMusicAndVideo)
    thread4.start()
    # thread5.start()
    # os.system('adb -s 1234567 root')
    # os.system('adb remount')
    # os.system(r'adb pull /data/anr/ D:\Monkey\log\\')

