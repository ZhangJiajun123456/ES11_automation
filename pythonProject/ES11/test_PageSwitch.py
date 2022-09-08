"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/24 9:50
@Author  : zhangjiajun
@Github  :
@Software: PyCharm
@File    : test_PageSwitch.py

功能页面切换测试
"操作步骤：
   1) 固定菜单页的切换:左右切换5次切换频率2s一次，循环操作，持续6小时
   2)固定菜单页的切换:上一页切换5次-下一页切换5次，切换频率2s一次，循环操作，持续6小时"

"""



import time
import threading
from ES11_automation.pythonProject.ES11.Common import common
import Ign_on
from ES11_automation.pythonProject.ES11.Common import CanMessage

vehicle = "1234567"
phone  = "3TG0221820007792"
device = common.Test(vehicle,phone)

class Test:
    def test_run(self):
        CanMessage.Test().driver()
        time.sleep(2)
        Ign_on.ign_on()
        time.sleep(30)
        t3 = threading.Thread(target=CanMessage.Test().run_0x2FB)
        t3.start()
        time.sleep(3)
        CanMessage.Test().run_0x244()

if __name__ == "__main__":
    Test().test_run()
