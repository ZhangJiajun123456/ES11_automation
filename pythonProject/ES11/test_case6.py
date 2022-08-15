"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/9 11:45
@Author  : starnight_cyber
@Github  : https://github.com/starnightcyber
@Software: PyCharm
@File    : test_case6.py
"""
import os
import logging as log
import pytest


class Test:
    def setup_class(self):
        pass

    def test_main(self):
        log.basicConfig(level = log.DEBUG)
        log.info
        print('aaa')
        pass

    def teardown_class(self):
        pass

if __name__ == "__main__":
    pytest.main(['-s','test_case6.py','--alluredir','./temp'])
    os.system('allure generate ./temp -o ../reports --clean')