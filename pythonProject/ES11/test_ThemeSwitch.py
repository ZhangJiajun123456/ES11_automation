"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/17 9:48
@Author  : zhangjiajun
@Github  : git@github.com:ZhangJiajun123456/ES11_automation.git
@Software: PyCharm
@File    : test_ThemeSwitch.py

主题切换
"操作步骤：
   1)主题切换，每间隔1s切换一次，循环切换，持续12小时"

"""
import time
import uiautomator2 as u2
import os
import threading
import test_CanSend
global zcanlib


d = u2.connect("1234567")


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
        ret1 = zcanlib.TransmitFD(chn_handle, msgs1, transmit_num1)
        time.sleep(0.5)

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
        ret2 = zcanlib.TransmitFD(chn_handle, msgs2, transmit_num2)
        time.sleep(0.5)

def DarkMode():
    d.xpath('//*[@text="Display"]').click()
    time.sleep(1)
    for i in range(2):
        d.swipe(1364, 151, 1364, 651)
        time.sleep(1)
    d.swipe(1364, 651, 1364, 151)
    time.sleep(1)
    os.system('adb -s 1234567 shell input tap 1000 500')
    time.sleep(1)


def LightMode():
    time.sleep(1)
    d.xpath('//*[@text="Display"]').click()
    time.sleep(1)
    for i in range(2):
        d.swipe(1364, 151, 1364, 651)
        time.sleep(1)
    d.swipe(1364, 651, 1364, 151)
    time.sleep(1)
    os.system('adb -s 1234567 shell input tap 1200 500')
    time.sleep(1)



def individual():
    d(resourceId="com.beantechs.settings:id/tv_control", text="Individual").click()
    time.sleep(1)
    d.xpath('//*[@text="Dashboard Screen"]').click()
    time.sleep(1)
    d.xpath('//*[@resource-id="com.beantechs.settings:id/rb_shoudong"]').click()
    d.swipe(500, 442, 500, 642)
    time.sleep(1)
    d.xpath('//*[@text="Digital Mode"]').click()
    time.sleep(1)
    d.xpath('//*[@text="Minimalist Mode"]').click()
    time.sleep(1)
    d.swipe(500, 642, 500, 442)
    time.sleep(1)
    d.xpath('//*[@text="ADAS Mode"]').click_exists(2)
    time.sleep(1)

def test_switch():
    try:
        while True:
            DarkMode()
            individual()
            LightMode()
            individual()
    except Exception as e:
        print(e)
    finally:
        test_switch()

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
    cmd = "adb -s 1234567 shell am start com.beantechs.settings/com.beantechs.settings.ui.activity.MainActivity"
    os.system(cmd)
    time.sleep(1)
    test_switch()
