"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/12 13:39
@Author  : zhangjiajun
@Github  :
@Software: PyCharm
@File    : test_CpuInfo.py
"""

import re
import subprocess
import pytest
import allure

@allure.description('测试CPU total占用率')
def test_main():
    cmd = "adb shell dumpsys cpuinfo"
    output = subprocess.Popen(cmd,stderr=subprocess.PIPE,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
    output = str(output.stdout.read())
    dd1 = re.findall(r"kernel\\r\\n(\d*)% TOTAL:", output)
    dd2 = int(dd1[0])
    assert dd2 > 8

if __name__ =='__main__':
    pytest.main(['-v'])