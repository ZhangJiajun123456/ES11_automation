"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/8 15:07
@Author  : Zhang jiajun
@Github  :
@Software: PyCharm
@File    : test_OnOff(KL30).py
开关机测试（KL30）
操作步骤：
1) KL30 on
2) 等待60s
3) KL30 off
4) 等待60s
5) 循环上述操作1000次
"""

"""通过serial串口进行通信，"""
import serial
import binascii
import time
from time import sleep
import win32api

# def pull_log():
#   cmd="D:\landmark\GAC_IVI\A58A88\GetLog\CatchLog\pull_log_python.bat"
#   win32api.ShellExecute(0, 'open', cmd, '', '', 1)  # 前台打开
#
# def clear_log():
#     cmd = "D:\landmark\GAC_IVI\A58A88\GetLog\CatchLog\clear_log_python.bat"
#     win32api.ShellExecute(0, 'open', cmd, '', '', 1)  # 前台打开

def ACC_off():
    print("拔掉ACC/IGN")
    a = 'FE 05 00 00 FF 00 98 35'  # 十六进制字符串。数据帧：控制第一路关
    d = bytes.fromhex(a)  # 十六进制字符串转bytes
    result = ser.write(d)  # 串口发送数据
    count = ser.inWaiting()  # 停止、等待数据，这一步非常关键。
    if count > 0:
        data = ser.read(count)  # 数据的接收
        if data != b'':
            # 将接受的16进制数据格式如b'h\x12\x90xV5\x12h\x91\n4737E\xc3\xab\x89hE\xe0\x16'
            #                      转换成b'6812907856351268910a3437333745c3ab896845e016'
            #                      通过[]去除前后的b'',得到我们真正想要的数据
            print("receive", str(binascii.b2a_hex(data))[2:-1])

def ACC_on():
    a1 = 'FE 05 00 00 00 00 D9 C5'  # 十六进制字符串。数据帧：控制第一路关
    d1 = bytes.fromhex(a1)  # 十六进制字符串转bytes
    result1 = ser.write(d1)  # 串口发送数据
    count = ser.inWaiting()  # 停止、等待数据，这一步非常关键。
    if count > 0:
        data = ser.read(count)  # 数据的接收
        if data != b'':
            # 将接受的16进制数据格式如b'h\x12\x90xV5\x12h\x91\n4737E\xc3\xab\x89hE\xe0\x16'
            #                      转换成b'6812907856351268910a3437333745c3ab896845e016'
            #                      通过[]去除前后的b'',得到我们真正想要的数据
            print("receive", str(binascii.b2a_hex(data))[2:-1])

if __name__ == "__main__":
    ser = serial.Serial("COM3", 9600, 8, "E", timeout=50, stopbits=1)  # 配置串口基本参数并建立通信
    for i in range(1000):
        ACC_off()
        print("开始进入休眠状态")
        time.sleep(60)
        ACC_on()
        print("退出休眠状态，进入唤醒状态")
        # time.sleep(120)
        # print("开始抓取log")
        # pull_log()
        # time.sleep(120)
        # print("开始删除log")
        # clear_log()
        time.sleep(60)
        print("已执行第%d次" % i)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 输出当前时间
        # """
        # print("等待5分钟进入休眠状态")
        # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 输出当前时间
        # time.sleep(300)
        # print("开始进入休眠状态")
        # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 输出当前时间
        # time.sleep(120)
        # print("进入唤醒状态")
        # time.sleep(120)
        # print("已执行第%d次" % i)
        # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 输出当前时间
        # """
    ser.close()  # 关闭串口
    sleep(1)
