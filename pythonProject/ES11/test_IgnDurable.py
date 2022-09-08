"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/25 10:05
@Author  : zhangjiajun
@Github  : git@github.com:ZhangJiajun123456/ES11_automation.git
@Software: PyCharm
@File    : test_IgnDurable.py
点火耐久自动化测试
操作步骤：
1) ACC ON
2) 等待1s
3) IG1 ON
4) 等待60s
5) IG1/ACC OFF
6) 等待60s
7) 循环上述操作1000次
"""
import os
import time
import threading
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
    count = 1
    while True:
        #创建线程进行acc状态
        t1 = threading.Thread(target=CanMessage.Test().run_0x295_acc)
        t2 = threading.Thread(target=CanMessage.Test().run_0x501)
        threads = [t1,t2]
        for t in threads:
            t.start()
        time.sleep(5)
        for t in threads:
            stopThread.stop_thread(t)
        time.sleep(5)
        #进入ign on
        #Send Can Message
        Ign_on.ign_on()
        threads = Ign_on.get_threads()
        time.sleep(60)
        #做截图对比，对比两图非100%一样则保存图片到TestPicture文件夹
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
        #关闭线程
        for t in range(2):
            stopThread.stop_thread(threads[t])
        # 进行ign off
        Ign_off.ign_off()
        time.sleep(60)
        print('时间到，成功关闭信号发送')
    # Close CAN
    CanMessage.Test().close_zcanpro()
if __name__ == "__main__":
    test_run()


