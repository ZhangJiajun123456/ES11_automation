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
import os
from ES11_automation.pythonProject.ES11.Common import common
import Ign_on
from ES11_automation.pythonProject.ES11.Common import CanMessage

vehicle = "1234567"
phone  = "3TG0221820007792"
device = common.Test(vehicle,phone)

class Test:
    def test_switch(self):
        try:
            while True:
                device.DarkMode()
                device.individual()
                device.LightMode()
                device.individual()
        except Exception as e:
            print(e)
        finally:
            Test().test_switch()
    #
    def test_run(self):
        CanMessage.Test().driver()
        time.sleep(2)
        Ign_on.ign_on()
        time.sleep(30)
        os.system('adb -s 1234567 shell am start com.beantechs.settings/com.beantechs.settings.ui.activity.MainActivity')
        time.sleep(1)
        Test().test_switch()

if __name__ == "__main__":
    Test().test_run()
