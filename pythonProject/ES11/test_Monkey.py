"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/9 11:45
@Author  : starnight_cyber
@Github  : https://github.com/starnightcyber
@Software: PyCharm
@File    : test_Monkey.py
"""
import os
import re
import subprocess
import threading
import time



class Test:
    def setup_class(self):
        pass
    def test1(self):
        time.sleep(43200)
        cmd2 = 'adb shell "ps | grep monkey"'
        output = subprocess.Popen(cmd2,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        output = output.stdout.read().decode()
        m1 = re.findall('root         (\d+)',output)
        m2 = re.findall('root          (\d+)',output)
        m3 = re.findall('root           (\d+)',output)
        cmd3 = 'adb shell "ps | grep logcat"'
        logcat = subprocess.Popen(cmd3,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        logcat = logcat.stdout.read().decode()
        m4 = re.findall('root         (\d+)',logcat)
        m5 = re.findall('root          (\d+)',logcat)
        m6 = re.findall('root           (\d+)',logcat)
        m = m1+m2+m3+m4+m5+m6
        print(m)
        for i in m:
            cmd4 = "adb shell kill " + i
            os.system(cmd4)
        os.system("adb root")
        os.system("adb remount")
        os.system(r"adb pull data/anr/ D:\Monkey\log\\")
    #
    #
    def test2(self):
        cmd1 = r"adb shell monkey --pct-syskeys 0 --pkg-whitelist-file /data/local/tmp/whitelist.txt -v -v -v --ignore-crashes --ignore-timeouts --throttle 500 250000000 > D:\Monkey\log\log.txt"
        os.system(cmd1)

    def test3(self):
        os.system(r"adb logcat -v time >D:\Monkey\log\logcat.txt")

    def teardown_class(self):
        pass

if __name__ == "__main__":
    os.system('adb logcat -c')
    os.system('adb shell rm -rf data/anr/')
    os.system('adb root')
    thread1 = threading.Thread(target=Test().test1)
    thread2 = threading.Thread(target=Test().test2)
    thread3 = threading.Thread(target=Test().test3)
    thread1.start()
    thread2.start()
    thread3.start()