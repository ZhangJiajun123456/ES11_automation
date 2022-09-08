"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/19 13:25
@Author  : zhangjiajun
@Github  :
@Software: PyCharm
@File    : Ign_on.py
"""

from ES11_automation.pythonProject.ES11.Common import CanMessage
import time
import threading
threads = []

def ign_on():
    global threads
    print('您好，尊贵的欧拉猫用户，有欧拉宠你,让你的生活更加多彩')
    t1 = threading.Thread(target=CanMessage.Test().run_0x295_on)
    t2 = threading.Thread(target=CanMessage.Test().run_0x501)
    t3 = threading.Thread(target=CanMessage.Test().run_0x345_Unlock)
    t4 = threading.Thread(target=CanMessage.Test().run_0x319_Open)
    threads = [t1,t2,t3,t4]
    for t in threads:
        t.start()


def get_threads():
    return threads





if __name__ == "__main__":
    CanMessage.Test().driver()
    time.sleep(2)
    ign_on()



