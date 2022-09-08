"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/24 15:37
@Author  : zhangjiajun
@Github  : git@github.com:ZhangJiajun123456/ES11_automation.git
@Software: PyCharm
@File    : Ign_off.py
"""
import time
import threading
from ES11_automation.pythonProject.ES11.Common import CanMessage
from ES11_automation.pythonProject.ES11.Common import stopThread

def ign_off():
    t1 = threading.Thread(target=CanMessage.Test().run_0x295_off)
    time.sleep(2)
    t2 = threading.Thread(target=CanMessage.Test().run_0x501)
    t3 = threading.Thread(target=CanMessage.Test().run_0x345_lock)
    time.sleep(2)
    t4 = threading.Thread(target=CanMessage.Test().run_0x319_Close)
    threads = [t1,t2]
    time.sleep(1)
    t1.start()
    time.sleep(2)
    t2.start()
    t3.start()
    time.sleep(2)
    t4.start()
    time.sleep(30)
    for t in threads:
        stopThread.stop_thread(t)




if __name__ == "__main__":
    CanMessage.Test().driver()
    time.sleep(2)
    ign_off()
