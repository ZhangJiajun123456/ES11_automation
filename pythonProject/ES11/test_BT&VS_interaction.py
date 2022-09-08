"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/08/26 17:08:46
@Author  : zhangjiajun
@Github  : git@github.com:ZhangJiajun123456/ES11_automation.git
@Software: PyCharm
@File    : test_BT&VS_interaction.py

蓝牙与车速交互
前提条件：
连接蓝牙且播放蓝牙音乐，车速持续发送中
1. 编写脚本模拟中控上操作执行
   1)在线音乐上一曲/下一曲，选取特定APP打开退出。循环操作12小时（间隔时间确认）
"""
import threading
import time
from Common import common
import Ign_on
from ES11_automation.pythonProject.ES11.Common import CanMessage




vehicle = "1234567"
phone  = "3TG0221820007792"
device = common.Test(vehicle,phone)
d1 = device.d1
d2 = device.d2

class Test:
    # 抓log
    # def catch_log(self):
    #     os.system("adb -s 1234567 logcat -c")
    #     os.system("adb -s 1234567 logcat -v time > D:\Monkey\log\crash.txt")
    def test_multi(self):
        try:
            device.close_VehicleBT()
            device.close_PhoneBT()
            device.BT_connect()
            time.sleep(2)
            device.play_BTmusic()
            time.sleep(1)
            while True:
                d1.xpath('//*[@resource-id="com.beantechs.mediacenter:id/next"]').click()
                time.sleep(1)
                d1.xpath('//*[@resource-id="com.beantechs.mediacenter:id/prev"]').click()
                time.sleep(1)
                d1.xpath('//*[@resource-id="com.android.systemui:id/applist_button"]').click()
                time.sleep(1)
                d1(text='Power Assistant').click()
                time.sleep(1)
                d1.xpath('//*[@resource-id="com.android.systemui:id/scene_cutover_button"]').click()
                time.sleep(1)
                d1(text='Bluetooth Music').click()
                time.sleep(1)
        except Exception as e:
            print(e)
        finally:
            Test().test_multi()

    def test_run(self):
        CanMessage.Test().driver()
        time.sleep(2)
        Ign_on.ign_on()
        time.sleep(5)
        t3 = threading.Thread(target=CanMessage.Test().run_137)
        t3.start()
        Test().test_multi()





if __name__ == "__main__":
    Test().test_run()




