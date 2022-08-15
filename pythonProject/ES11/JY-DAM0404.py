# -*- coding: utf-8 -*-

"""
休眠唤醒测试（KL15）
操作步骤：
1) KL15 on
2) 等待60s
3) KL15 off
4) 等待60s
5) 循环上述操作1000次
"""


# import serial
# import modbus_tk
# # import modbus_tk.defines as cst
# from modbus_tk import modbus_rtu
# #



"""继电器支持usb，通过modbus协议控制继电器"""
# #port:串口号； baudrate：波特率
# master = modbus_rtu.RtuMaster(serial.Serial(port="COM3", baudrate=9600, bytesize=8, parity='N', stopbits=1))
# master.set_timeout(5.0)
# print(master)
#
# #测试首先使用读取测试，防止写入错误参数
# #2为站点号slave；cst.READ_HOLDING_REGISTERS读取保持寄存器，1为读取的寄存器开始地址，8为读取寄存器的个数
# tt = master.execute(1, cst.READ_HOLDING_REGISTERS, 1, 1)
# print(tt)
#

# #写入操作当对动作指令寄存器写入对应动作参数，就会立刻进行执行动作
# #2位站点号；cst.WRITE_SINGLE_REGISTER写入单个寄存器；100寄存器写入地址；output_value写入的值
# # master.execute(2, cst.WRITE_SINGLE_REGISTER, 100, output_value=13)
#
#
# #2位站点号；cst.WRITE_SINGLE_REGISTER写入单个寄存器；1寄存器写入起始地址；output_value写入的值，此为连续地址写入
# # master.execute(2, cst.WRITE_MULTIPLE_REGISTERS, 1, output_value=[0, 0, 0, 0])

import serial
# import modbus_tk
# import modbus_tk.defines as cst
# from modbus_tk import modbus_rtu


# def mod(PORT="com3"):
#     red = []
#     alarm = ""
#     try:
#         # 设定串口为从站
#         master = modbus_rtu.RtuMaster(serial.Serial(port=PORT,
#                                                     baudrate=9600, bytesize=8, parity='N', stopbits=1))
#         master.set_timeout(5.0)
#         master.set_verbose(True)
#
#         # 读保持寄存器
#         red = master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 9)  # 这里可以修改需要读取的功能码
#         print(red)
#         alarm = "正常"
#         return list(red), alarm
#
#     except Exception as exc:
#         print(str(exc))
#         alarm = (str(exc))
#
#     return red, alarm  ##如果异常就返回[],故障信息
#
#
# if __name__ == "__main__":
#     mod()

"""继电器支持wifi，通过socket控制继电器"""
# import time
# import socket
#
# print(time.localtime(time.time()))
#
# datas = {
#     "SetOnOrder": {
#         "0": "fe050000ff009835",
#         "1": "fe050001ff00c9f5",
#         "2": "fe050002ff0039f5",
#         "3": "fe050003ff006835",
#         "4": "fe050004ff00d9f4",
#         "5": "fe050005ff008834",
#         "6": "fe050006ff007834",
#         "7": "fe050007ff0029f4",
#         "8": "fe050008ff0019f7",
#         "9": "fe050009ff004837",
#         "10": "fe05000aff00b837",
#         "11": "fe05000bff00e9f7",
#         "12": "fe05000cff005836",
#         "13": "fe05000dff0009f6",
#         "14": "fe05000eff00f9f6",
#         "15": "fe05000fff00a836"
#
#     },
#     "SetOffOrder": {
#         "0": "fe0500000000d9c5",
#         "1": "fe05000100008805",
#         "2": "fe05000200007805",
#         "3": "fe050003000029c5",
#         "4": "fe05000400009804",
#         "5": "fe0500050000c9c4",
#         "6": "fe050006000039c4",
#         "7": "fe05000700006804",
#         "8": "fe05000800005807",
#         "9": "fe050009000009c7",
#         "10": "fe05000a0000f9c7",
#         "11": "fe05000b0000a807",
#         "12": "fe05000c000019c6",
#         "13": "fe05000d00004806",
#         "14": "fe05000e0000b806",
#         "15": "fe05000f0000e9c6"
#
#     }
# }
#
#
#
# def callPower(ip, port, order):
#     s = socket.socket()
#     s.connect((ip, port))
#     Modbus_16 = ""
#     for x in range(0, len(order), 2):
#         Modbus_16 += chr(int(order[x:x + 2], 16))
#
#     s.send(Modbus_16.encode('ISO-8859-1'))
#     reply_16 = s.recv(50)
#
#     reply_temp = ""
#     for i in reply_16.decode('ISO-8859-1'):
#         reply_temp += "0x%02x" % ord(i)
#     reply_temp = reply_temp[2:]
#     mb = ""
#     while reply_temp:
#         mb += reply_temp[0:2]
#         reply_temp = reply_temp[4:]
#     return mb
#
#
# IP = "192.168.3.125"
# port = 10000
# roads = 8
# for s in range(100):
#     for orderSet in datas:
#         if orderSet == "SetOnOrder":
#             for j in range(roads):
#                 order = datas["SetOnOrder"][str(j)]
#                 print("发：", order)
#                 for i in range(25):
#                     mb = callPower(IP, port, order)
#                     print("收：", mb)
#                     if mb != order:
#                         continue
#                     break
#                 print("第" + str(j + 1) + "路打开指令已发送")
#                 j += 1
#         else:
#             for k in range(roads):
#                 order = datas["SetOffOrder"][str(k)]
#                 print("发：", order)
#                 for t in range(25):
#                     mb = callPower(IP, port, order)
#                     print("收：", mb)
#                     if mb != order:
#                         time.sleep(0.3)
#                         continue
#                     break
#                 print("第" + str(k + 1) + "路关闭指令已发送")
#                 k += 1
#     s += 1
#     print(time.localtime(time.time()))
#     print(f"-------第{s}次循环已完成---------")
#
#
# print(time.localtime(time.time()))

"""通过模拟点击PC上JYDAM软件实现继电器的开/关效果"""
# import lackey
# import time
# from pywinauto import application
# import pywinauto
# from pywinauto import mouse
# from pywinauto import keyboard

# path ="D:/自动化测试资料/文档/继电器说明文档/JYDAM调试软件/JYDAM.exe"
# app = application.Application(backend='win32').start(path)  # 启动zcanpro
# # dialogWindow = pywinauto.application.Application().connect(class_name="#32770 (Dialog)")
# # window = dialogWindow.top_window()
# # window.type_keys("")
# # time.sleep(10)
# # mouse.click(coords=(984, 66))
# time.sleep(5)
# lackey.click('D:/landmark/GAC_IVI/04SystemTest/picture/open_port.png')  # 点击发送数据
# time.sleep(5)
# lackey.click('D:/landmark/GAC_IVI/04SystemTest/picture/DO1.png')  # 点击发送数据

"""通过serial串口进行通信，"""
import serial
import binascii
import time
import os
from time import sleep
import win32api

def pull_log():
  cmd="D:\landmark\GAC_IVI\A58A88\GetLog\CatchLog\pull_log_python.bat"
  win32api.ShellExecute(0, 'open', cmd, '', '', 1)  # 前台打开

def clear_log():
    cmd = "D:\landmark\GAC_IVI\A58A88\GetLog\CatchLog\clear_log_python.bat"
    win32api.ShellExecute(0, 'open', cmd, '', '', 1)  # 前台打开

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
    for i in range(5):
        ACC_off()
        print("开始进入休眠状态")
        time.sleep(60)
        ACC_on()
        print("退出休眠状态，进入唤醒状态")
        time.sleep(120)
        print("开始抓取log")
        pull_log()
        time.sleep(120)
        print("开始删除log")
        clear_log()
        # time.sleep(60)
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
