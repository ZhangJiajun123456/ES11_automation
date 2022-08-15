"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/9 10:44
@Author  : starnight_cyber
@Github  : https://github.com/starnightcyber
@Software: PyCharm
@File    : test_pyhello.py
"""

import pytest

class Test:
    def test_hello(self):
        print('6666')

    def test_hello2(self):
        print('7777')
        raise Exception("跳出异常")

if __name__ == "__main__":
    pytest.main()