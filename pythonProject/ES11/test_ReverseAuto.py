"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/24 15:19
@Author  : zhangjiajun
@Github  : git@github.com:ZhangJiajun123456/ES11_automation.git
@Software: PyCharm
@File    : test_ReverseAuto.py
倒车自动化测试
操作步骤：
   1)设置开机
   2)设置等待时间（40s)，
   3)发送信号进入倒车画面
   4)间隔60s
   5)设置关机
   6)持续12小时以上
"""
import time
import os
from Common import common
from Common import screen_compare as sc
import Ign_on
from ES11_automation.pythonProject.ES11.Common import CanMessage
from Common import stopThread
import Ign_off

vehicle = "1234567"
phone  = "3TG0221820007792"
device = common.Test(vehicle,phone)

def test_run():
    CanMessage.Test().driver()
    time.sleep(2)
    count = 1
    while True:
        Ign_on.ign_on()
        threads = Ign_on.get_threads()
        time.sleep(60)
        os.system('adb -s 1234567 shell am start com.beantechs.mediacenter/com.beantechs.mediacenter.ui.LaunchActivity')
        time.sleep(2)
        # 做截图对比，对比两图非100%一样则保存图片到TestPicture文件夹
        device.d1.screenshot('../../TestPicture/' + str(count) + '.png')
        time.sleep(2)
        sc.screenshot(str(count) + '.png', (120, 463, 1182, 603), str(count) + '.png')
        time.sleep(2)
        res = sc.image_contrast('ign_on.png', str(count) + '.png')
        time.sleep(2)
        if res != 0.0:
            print('图片对比失败')
        else:
            os.system('del D:\ES11\ES11_automation\TestPicture\\' + str(count) + '.png')
            print('图片比对成功')
        count = count + 1
        time.sleep(2)
        CanMessage.Test().run_29F()
        time.sleep(5)
        #关闭线程
        for t in range(2):
            stopThread.stop_thread(threads[t])
        Ign_off.ign_off()
        time.sleep(60)
        print('时间到，成功关闭信号发送')
    CanMessage.Test().close_zcanpro()

if __name__ == "__main__":
    test_run()


