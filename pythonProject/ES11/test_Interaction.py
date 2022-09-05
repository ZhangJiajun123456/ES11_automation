"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/08/30 13:25:19
@Author  : zhangjiajun
@Github  : git@github.com:ZhangJiajun123456/ES11_automation.git
@Software: PyCharm
@File    : test_Interaction.py

中控仪表交互测试脚本
操作步骤：
   1)进行音乐操作（暂停-播放-下一首-上一首），切换到播放FM（暂停-播放-上一台-下一台），切换主题。
   2) 音乐播放中拨打电话等待5s挂断电话，切换主题
   3) FM电台播放中，拨打电话等待5s挂断电话，切换主题。
   5) 操作音乐功能，切换播放FM
   6) 操作音乐功能，拨打电话等待5s挂断
   7) 播放FM，拨打电话等待5s挂断
   8) 搭配仪表车速脚本同步循环以上操作，持续12小时"
"""


import os
import time

from Common import common
vehicle = "1234567"
phone  = "3TG0221820007792"
device = common.Test(vehicle,phone)

def test_interaction():
    try:
        #判断蓝牙是否连接
        os.system('adb -s 1234567 shell am start com.beantechs.settings/com.beantechs.settings.ui.activity.MainActivity')
        #判断BT是否连接
        time.sleep(2)
        if not device.d1(text='DISCONNECT').exists(timeout=3):
            device.BT_connect()
            time.sleep(1)
        # 播放音乐
        while True:
            device.play_BTmusic()
            time.sleep(2)
            #歌曲切换
            device.d1(resourceId='com.beantechs.mediacenter:id/next').click()
            time.sleep(1)
            device.d1(resourceId='com.beantechs.mediacenter:id/prev').click()
            time.sleep(1)
            #切换至FM
            device.d1(resourceId='com.beantechs.mediacenter:id/tab_local_radio').click()
            time.sleep(1)
            device.d1(resourceId='com.beantechs.mediacenter:id/tv_fm').click()
            time.sleep(1)
            device.d1(resourceId='com.beantechs.mediacenter:id/iv_control').click()
            time.sleep(1)
            device.d1(resourceId='com.beantechs.mediacenter:id/iv_control_next').click()
            time.sleep(1)
            device.d1(resourceId='com.beantechs.mediacenter:id/iv_control_pre').click()
            time.sleep(1)
            #切换主题
            cmd = "adb -s 1234567 shell am start com.beantechs.settings/com.beantechs.settings.ui.activity.MainActivity"
            os.system(cmd)
            device.d1(resourceId="com.beantechs.settings:id/tv_control", text="Individual").click()
            time.sleep(1)
            device.d1.xpath('//*[@text="Dashboard Screen"]').click()
            time.sleep(1)
            device.d1.xpath('//*[@resource-id="com.beantechs.settings:id/rb_shoudong"]').click()
            device.d1.swipe(500, 442, 500, 642)
            time.sleep(1)
            device.d1.xpath('//*[@text="Minimalist Mode"]').click()
            #切回蓝牙音乐播放
            os.system('adb -s 1234567 shell am start com.beantechs.mediacenter/com.beantechs.mediacenter.ui.HomeActivity')
            time.sleep(1)
            device.d1.xpath('//*[@resource-id="com.beantechs.mediacenter:id/tab_bt_music"]/android.widget.FrameLayout[1]').click()
            time.sleep(1)
            device.d1(resourceId='com.beantechs.mediacenter:id/play_pause').click()
            time.sleep(1)
            device.d1(resourceId='com.beantechs.mediacenter:id/play_pause').click()
            time.sleep(1)
            #拨打电话
            device.call_vehicleside(10010)
            time.sleep(5)
            #挂断电话
            device.endcall_vehicleside()
            time.sleep(1)
            # 切换主题
            cmd = "adb -s 1234567 shell am start com.beantechs.settings/com.beantechs.settings.ui.activity.MainActivity"
            os.system(cmd)
            device.d1(resourceId="com.beantechs.settings:id/tv_control", text="Individual").click()
            time.sleep(1)
            device.d1.xpath('//*[@text="Dashboard Screen"]').click()
            time.sleep(1)
            device.d1.xpath('//*[@resource-id="com.beantechs.settings:id/rb_shoudong"]').click()
            device.d1.swipe(500, 442, 500, 642)
            time.sleep(1)
            device.d1.swipe(500, 642, 500, 442)
            time.sleep(1)
            device.d1.xpath('//*[@text="ADAS Mode"]').click_exists(2)
            #切回FM播放然后拨打电话
            device.d1(resourceId='com.beantechs.mediacenter:id/tab_local_radio').click()
            time.sleep(1)
            device.d1(resourceId='com.beantechs.mediacenter:id/tv_fm').click()
            time.sleep(1)
            device.call_vehicleside(10010)
            time.sleep(5)
            device.endcall_vehicleside()
            time.sleep(1)
            #挂断电话
            device.endcall_vehicleside()
            # 切换主题
            cmd = "adb -s 1234567 shell am start com.beantechs.settings/com.beantechs.settings.ui.activity.MainActivity"
            os.system(cmd)
            device.d1(resourceId="com.beantechs.settings:id/tv_control", text="Individual").click()
            time.sleep(1)
            device.d1.xpath('//*[@text="Dashboard Screen"]').click()
            time.sleep(1)
            device.d1.xpath('//*[@resource-id="com.beantechs.settings:id/rb_shoudong"]').click()
            device.d1.swipe(500, 442, 500, 642)
            time.sleep(1)
            device.d1.xpath('//*[@text="Digital Mode"]').click()
    except Exception as e:
        print(e)
    finally:
        test_interaction()

if __name__ == "__main__":
    test_interaction()


