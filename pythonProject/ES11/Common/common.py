"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/25 11:07
@Author  : zhangjiajun
@Github  : git@github.com:ZhangJiajun123456/ES11_automation.git
@Software: PyCharm
@File    : common.py
"""
import os
import time
import uiautomator2 as u2
import screen_compare as sc
vehicle = "1234567"
phone  = "3TG0221820007792"
d1 = ''
d2 = ''

class Test:

    def __init__(self,vehicle,phone):
        self.vehicle = vehicle
        self.phone = phone
        self.d1 = u2.connect(vehicle)
        self.d2 = u2.connect(phone)
        self.d2.implicitly_wait(20)
    #蓝牙连接
    def BT_connect(self):
        os.system('adb -s 1234567 shell am start com.beantechs.settings/com.beantechs.settings.ui.activity.MainActivity')
        time.sleep(2)
        self.d1.xpath('//*[@resource-id="com.beantechs.settings:id/rv_control"]/android.view.ViewGroup[1]/android.widget.TextView[1]').click()
        time.sleep(2)
        res = self.d1(resourceId="com.beantechs.settings:id/sw_ble").get_text()
        if res == "OFF":
            self.d1.xpath('//*[@resource-id="com.beantechs.settings:id/sw_ble"]').click()
        time.sleep(2)
        self.d2.press('home')  #回到home
        time.sleep(2)
        self.d2(text="设置").click()
        time.sleep(2)
        for i in range(2):
            self.d2.swipe(216,591,216,1887)
            time.sleep(1)
        self.d2(text="蓝牙").click()
        time.sleep(2)
        res = self.d2(resourceId="com.android.settings:id/switch_widget").info
        if res['checked'] != True:
            self.d2.xpath('//*[@resource-id="com.android.settings:id/switch_widget"]').click()
        if self.d2(text = "ORA_1266").exists(timeout=10):
            print('找到了')
            self.d2(text = "ORA_1266").click()
        else:
            for i in range(3):
                self.d2.swipe(192,1973,192,1133)
                time.sleep(1)
                if self.d2(text = "ORA_1266").exists(timeout=10):
                    self.d2(text="ORA_1266").click()
                    break
        time.sleep(1)
        self.d1(text = "PAIR").click()
        if self.d2(text = "配对").exists(timeout=5):
            self.d2(text = "配对").click()
            time.sleep(2)
        if self.d2(text = "允许").exists(timeout=5):
            self.d2(text = "允许").click()

    #车机端断连BT
    def BT_disconnect_vehicle(self):
        os.system('adb -s 1234567 shell am start com.beantechs.settings/com.beantechs.settings.ui.activity.MainActivity')
        time.sleep(2)
        self.d1.xpath('//*[@resource-id="com.beantechs.settings:id/rv_control"]/android.view.ViewGroup[1]/android.widget.TextView[1]').click()
        time.sleep(2)
        self.d1(text = 'DISCONNECT').click(timeout=5)
        time.sleep(2)
    #手机端断连BT
    def BT_disconnect_phone(self):
        self.d2.press('home')  # 回到home
        time.sleep(2)
        self.d2(text="设置").click()
        time.sleep(2)
        for i in range(2):
            self.d2.swipe(216, 591, 216, 1887)
            time.sleep(1)
        self.d2(text="蓝牙").click()
        time.sleep(2)
        for i in range(3):
            time.sleep(8)
            if  self.d2(text="ORA_1266").exists(timeout=5):
                self.d2(text="ORA_1266").click()
                time.sleep(2)
            if  self.d2(text="确定").exists(timeout=5):
                self.d2(text="确定").click()
                time.sleep(2)
                break
            else:
                self.d2.swipe(192, 1133, 192, 1973)

    #车机端重连BT
    def BT_reconnect(self):
        os.system('adb -s 1234567 shell am start com.beantechs.settings/com.beantechs.settings.ui.activity.MainActivity')
        time.sleep(2)
        self.d1.xpath('//*[@resource-id="com.beantechs.settings:id/rv_control"]/android.view.ViewGroup[1]/android.widget.TextView[1]').click()
        time.sleep(2)
        self.d1(text='CONNECT').click()
        time.sleep(2)

     #取消配对并关闭车机蓝牙
    def close_VehicleBT(self):
        os.system('adb -s 1234567 shell am start com.beantechs.settings/com.beantechs.settings.ui.activity.MainActivity')
        time.sleep(2)
        self.d1.xpath('//*[@text="Bluetooth"]').click()
        time.sleep(2)
        if self.d1(resourceId='com.beantechs.settings:id/sw_ble').info['text']!='ON':
            self.d1.xpath('//*[@resource-id="com.beantechs.settings:id/sw_ble"]').click()
            time.sleep(5)
        while True:
            if self.d1(resourceId='com.beantechs.settings:id/bt_ble_current_delete').exists(timeout=3):
                self.d1(resourceId='com.beantechs.settings:id/bt_ble_current_delete').click()
                time.sleep(2)
            elif self.d1(resourceId='com.beantechs.settings:id/bt_item_delete').exists(timeout=3):
                self.d1(resourceId='com.beantechs.settings:id/bt_item_delete').click()
                time.sleep(2)
            else:
                break
        time.sleep(2)
        self.d1.xpath('//*[@resource-id="com.beantechs.settings:id/sw_ble"]').click()
        time.sleep(2)

    #取消配对并关闭手机蓝牙
    def close_PhoneBT(self):
        self.d2.press('home')  # 回到home
        time.sleep(2)
        self.d2(text="设置").click()
        time.sleep(2)
        for i in range(2):
            self.d2.swipe(216, 591, 216, 1887)
            time.sleep(1)
        self.d2(text="蓝牙").click()
        time.sleep(2)
        if not self.d2(resourceId='com.android.settings:id/switch_widget').info['checked']:
            self.d2(resourceId='com.android.settings:id/switch_widget').click()
            time.sleep(2)
        while True:
            if self.d2(description='详情按钮').exists:
                self.d2(description='详情按钮').click()
                time.sleep(2)
                self.d2(text="取消配对").click()
                time.sleep(2)
            else:
                break
        time.sleep(2)
        self.d2.xpath('//*[@resource-id="com.android.settings:id/switch_widget"]').click()

    #播放蓝牙音乐
    def play_BTmusic(self):
        self.d2.press('home')  # 回到home
        time.sleep(2)
        if self.d2(text='音乐').exists(timeout=3):
            self.d2(text='音乐').click()
            # time.sleep(2)
            # self.d2(resourceId='d(resourceId="com.huawei.music:id/mcseekbar")').click(timeout=3)
        os.system('adb -s 1234567 shell am start com.beantechs.mediacenter/com.beantechs.mediacenter.ui.HomeActivity')
        time.sleep(2)
        self.d1.xpath('//*[@resource-id="com.beantechs.mediacenter:id/tab_bt_music"]/android.widget.FrameLayout[1]').click()
        time.sleep(2)
        self.d1.screenshot(r'D:\ES11\ES11_automation\TestPicture\01.png')
        sc.screenshot('01.png',(896,544,1032,680),'01.png')
        time.sleep(2)
        res = sc.image_contrast('pause_status.png','01.png')
        print(res)
        if res == 0.0:
            self.d1.xpath('//*[@resource-id="com.beantechs.mediacenter:id/play_pause"]').click()
        time.sleep(2)


    #拨打电话
    def call_vehicleside(self,phoneNumber):
        os.system('adb -s 1234567 shell am start com.beantechs.btphone/com.beantechs.btphone.activity.MainActivity')
        time.sleep(1)
        self.d1.xpath('//*[@resource-id="com.beantechs.btphone:id/main_dialpad_del_btn"]').long_click()
        num = str(phoneNumber)
        for i in num:
            i = int(i)
            if i == 0:
                self.d1.xpath('//*[@resource-id="com.beantechs.btphone:id/num_recycler"]/android.widget.LinearLayout[11]').click()
            elif i == 1:
                self.d1.xpath('//*[@resource-id="com.beantechs.btphone:id/num_recycler"]/android.widget.LinearLayout[1]').click()
            elif i == 2:
                self.d1.xpath('//*[@resource-id="com.beantechs.btphone:id/num_recycler"]/android.widget.LinearLayout[2]').click()
            elif i == 3:
                self.d1.xpath('//*[@resource-id="com.beantechs.btphone:id/num_recycler"]/android.widget.LinearLayout[3]').click()
            elif i == 4:
                self.d1.xpath('//*[@resource-id="com.beantechs.btphone:id/num_recycler"]/android.widget.LinearLayout[4]').click()
            elif i == 5:
                self.d1.xpath('//*[@resource-id="com.beantechs.btphone:id/num_recycler"]/android.widget.LinearLayout[5]').click()
            elif i == 6:
                self.d1.xpath('//*[@resource-id="com.beantechs.btphone:id/num_recycler"]/android.widget.LinearLayout[6]').click()
            elif i == 7:
                self.d1.xpath('//*[@resource-id="com.beantechs.btphone:id/num_recycler"]/android.widget.LinearLayout[7]').click()
            elif i == 8:
                self.d1.xpath('//*[@resource-id="com.beantechs.btphone:id/num_recycler"]/android.widget.LinearLayout[8]').click()
            elif i == 9:
                self.d1.xpath('//*[@resource-id="com.beantechs.btphone:id/num_recycler"]/android.widget.LinearLayout[9]').click()
            time.sleep(0.5)
        self.d1(resourceId='com.beantechs.btphone:id/main_dial_btn').click()


    #挂断电话
    def endcall_vehicleside(self):
        os.system('adb -s 1234567 shell am start com.beantechs.btphone/com.beantechs.btphone.activity.MainActivity')
        time.sleep(1)
        if self.d1.xpath('//*[@resource-id="com.beantechs.btphone:id/incaller_terminate_btn"]').exists:
            self.d1.xpath('//*[@resource-id="com.beantechs.btphone:id/incaller_terminate_btn"]').click()
        elif self.d1.xpath('//*[@resource-id="com.beantechs.btphone:id/tv_title_content"]').exists:
            self.d1.xpath('//*[@resource-id="com.beantechs.btphone:id/tv_title_content"]').click()
            time.sleep(1)
            self.d1.xpath('//*[@resource-id="com.beantechs.btphone:id/incaller_terminate_btn"]').click()


    #关闭弹窗Telephone isn't responding
    def close_noRespondingWindow(self):
        time.sleep(2)
        if self.d1(text='Telephone isn\'t responding').exists:
            self.d1(text='Close app').click()
            time.sleep(2)
            
    #切换黑夜模式
    def DarkMode(self):
        self.d1.xpath('//*[@text="Display"]').click()
        time.sleep(1)
        for i in range(2):
            self.d1.swipe(1364, 151, 1364, 651)
            time.sleep(1)
        self.d1.swipe(1364, 651, 1364, 151)
        time.sleep(1)
        os.system('adb -s 1234567 shell input tap 1000 500')
        time.sleep(1)
        
    #切换白天模式
    def LightMode(self):
        time.sleep(1)
        self.d1.xpath('//*[@text="Display"]').click()
        time.sleep(1)
        for i in range(2):
            self.d1.swipe(1364, 151, 1364, 651)
            time.sleep(1)
        self.d1.swipe(1364, 651, 1364, 151)
        time.sleep(1)
        os.system('adb -s 1234567 shell input tap 1200 500')
        time.sleep(1)
        
    #切换模式
    def individual(self):
        self.d1(resourceId="com.beantechs.settings:id/tv_control", text="Individual").click()
        time.sleep(1)
        self.d1.xpath('//*[@text="Dashboard Screen"]').click()
        time.sleep(1)
        self.d1.xpath('//*[@resource-id="com.beantechs.settings:id/rb_shoudong"]').click()
        self.d1.swipe(500, 442, 500, 642)
        time.sleep(1)
        self.d1.xpath('//*[@text="Digital Mode"]').click()
        time.sleep(1)
        self.d1.xpath('//*[@text="Minimalist Mode"]').click()
        time.sleep(1)
        self.d1.swipe(500, 642, 500, 442)
        time.sleep(1)
        self.d1.xpath('//*[@text="ADAS Mode"]').click_exists(2)
        time.sleep(1)



    
