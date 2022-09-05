"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/08/30 09:31:40
@Author  : zhangjiajun
@Github  : git@github.com:ZhangJiajun123456/ES11_automation.git
@Software: PyCharm
@File    : test_BtPhone.py

蓝牙电话压测脚本
"操作步骤：
   1)播放蓝牙音乐
   2)拨打电话
   3)等待10s
   4)挂断电话
   5)等待10s
   6)重复操作以上步骤持续12小时"

"""
import os
import time

from Common import common
vehicle = "1234567"
phone  = "3TG0221820007792"
device = common.Test(vehicle,phone)

def test_phoneCall():
    try:
        os.system('adb -s 1234567 shell am start com.beantechs.settings/com.beantechs.settings.ui.activity.MainActivity')
        #判断BT是否连接
        if not device.d1(text='DISCONNECT').exists(timeout=3):
            device.BT_connect()
            time.sleep(1)
        while True:
            #播放音乐
            device.play_BTmusic()
            time.sleep(2)
            #车机端打电话，参数为需拨打的电话号码
            device.call_vehicleside(10010)
            time.sleep(10)
            #车机端挂断电话
            device.endcall_vehicleside()
    except Exception as e:
        print(e)
    finally:
        test_phoneCall()

if __name__ == "__main__":
    test_phoneCall()
