"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/9 16:10
@Author  : starnight_cyber
@Github  :
@Software: PyCharm
@File    : run_TestCase.py
"""
import subprocess
import sys

import pytest
import os
if __name__ == "__main__":
    # abspath = os.getcwd()
    # print(abspath)
    cmd1 = "pytest TestCase --alluredir reports/allure_raw"
    # pytest.main(['TestCase/', "--alluredir", "/reports/allure_raw"])
    os.system(cmd1)
    cmd2 = "allure generate reports/allure_raw -o reports/allure_report --clean"
    os.system(cmd2)


