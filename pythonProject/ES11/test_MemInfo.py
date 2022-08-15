"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/12 15:17
@Author  : zhangjiunjun
@Github  :
@Software: PyCharm
@File    : test_MemInfo.py
"""
import allure
import subprocess
import re


@allure.description('测试CPU total占用率')
def test_main():
    cmd = "adb shell dumpsys meminfo"
    output = subprocess.Popen(cmd,stderr=subprocess.PIPE,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
    output = str(output.stdout.read())
    print(output)
    # dd1 = re.findall(r"Total RAM: (\d*)", output)
    dd1 = re.findall(r"Total RAM: \d\,",output)
    print(dd1)

if __name__ == "__main__":
    test_main()

