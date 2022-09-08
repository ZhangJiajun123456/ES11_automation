"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/08/29 18:07:30
@Author  : zhangjiajun
@Github  : git@github.com:ZhangJiajun123456/ES11_automation.git
@Software: PyCharm
@File    : test_Chime.py
Chime测试
操作步骤：
  1) 录制Chime模块中车门开启指示灯报警音、前碰预警报警音、安全带未系报警音、超速报警等信号， 每隔0.5s激活一个，激活所有
  2) 持续12小时以上
"""

import time
from ES11_automation.pythonProject.ES11.Common import CanMessage
import Ign_on
        
def test_run():
    CanMessage.Test().driver()
    time.sleep(2)
    Ign_on.ign_on()
    time.sleep(30)
    CanMessage.Test().test_chime()


if __name__ == "__main__":
    test_run()



