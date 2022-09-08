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
import threading
import time
import Ign_on
from ES11_automation.pythonProject.ES11.Common import CanMessage


class Test:
    #抓log
    # def catch_log(self):
    #     os.system("adb -s 1234567 logcat -c")
    #     os.system("adb -s 1234567 logcat -v time > D:\Monkey\log\crash.txt")
  def test_run(self):
        CanMessage.Test().driver()
        time.sleep(2)
        Ign_on.ign_on()
        time.sleep(5)
        t3 = threading.Thread(target=CanMessage.Test().run_137)
        t3.start()
if __name__ == "__main__":
    Test().test_run()

