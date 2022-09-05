"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/26 11:38
@Author  : zhangjiajun
@Github  : git@github.com:ZhangJiajun123456/ES11_automation.git
@Software: PyCharm
@File    : test_BtConnect.py
蓝牙连接压测
操作步骤：
   1)手机蓝牙连接车机
   2)等待60s
   3)车机端断连蓝牙
   4)等待60s
   5)车机蓝牙重连
   6)等待60s
   7)手机端断连蓝牙
   8)等待60s
   9)重复操作以上步骤持续12小时
"""

import time
from Common import common
vehicle = "1234567"
phone  = "3TG0221820007792"
device = common.Test(vehicle,phone)


def test_btConnect():
    try:
        while True:
            device.BT_connect()
            time.sleep(3)
            device.BT_disconnect_vehicle()
            time.sleep(3)
            device.BT_reconnect()
            time.sleep(3)
            device.BT_disconnect_phone()
            time.sleep(3)
            device.close_BT()
            time.sleep(3)
    except Exception as e:
        print(e)
    finally:
        test_btConnect()

if __name__ == "__main__":
    test_btConnect()