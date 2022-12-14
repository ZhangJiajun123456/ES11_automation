"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/8 16:31
@Author  : Zhang jiajun
@Github  :
@Software: PyCharm
@File    : test_HighLoad.py

操作步骤：
  1) 录制warning模块中的安全带报警，胎压报警，水温报警，超速报警，esp报警，车门开关等信号， 每隔1s激活一个，激活所有有效果信号
  2) 录制tripComputer模块中胎压，胎温等信号， 每隔1s激活一个，激活所有有效果信号
  3) 录制display模块中驾驶模式，挡位， 每隔1s激活一个，激活所有有效果信号
  4) 录制TT模块中限速标志(TSR)指示灯、车门开启指示灯、安全气囊指示灯、前碰预警状态指示灯等信号，每隔1s激活一个，激活所有有效果信号
  5) 录制Chime模块中车门开启指示灯报警音、前碰预警报警音、TSR超速报警音等信号，每隔1s激活一个，激活所有有效果信号
  6) 录制gauge模块中车速指针，转速指针，水温表的变化，从低到高，从高到低，循环变化
  7) 以上内容组合到一起执行，持续12小时以上
"""

import time
from ES11_automation.pythonProject.ES11.Common import CanMessage
import Ign_on


def test_run():
    CanMessage.Test().driver()
    time.sleep(2)
    Ign_on.ign_on()
    time.sleep(30)
    CanMessage.Test().test_highload()

if __name__ == "__main__":
    test_run()
