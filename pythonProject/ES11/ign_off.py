"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/24 15:37
@Author  : zhangjiajun
@Github  : git@github.com:ZhangJiajun123456/ES11_automation.git
@Software: PyCharm
@File    : ign_off.py
"""
import time
import threading
import test_CanSend
import Ign_on
global zcanlib
global chn_handle
import ctypes
import inspect

# zcanlib = test_CanSend.ZCAN()
# handle = zcanlib.OpenDevice(test_CanSend.ZCAN_USBCANFD_200U, 0, 0)
# if handle == test_CanSend.INVALID_DEVICE_HANDLE:
#     print("Open Device failed!")
#     exit(0)
# print("device handle:%d." % (handle))
#
# info = zcanlib.GetDeviceInf(handle)
# print("Device Information:\n%s" % (info))
# #
# # Start CAN
# chn_handle = test_CanSend.can_start(zcanlib, handle, 0)
# print("channel handle:%d." % (chn_handle))

def run_0x501():
    transmit_num2 = 1
    msgs2 = test_CanSend.ZCAN_TransmitFD_Data()
    for i in range(transmit_num2):
        msgs2.transmit_type = 0
        msgs2.frame.eff = 0
        msgs2.frame.rtr = 0
        msgs2.frame.can_id = int('501', 16)
        msgs2.frame.len = 8
        str2 = "00 00 00 00 00 00 00 00"
        data2 = str2.split(' ')
        msgs2.frame.data[0] = int(data2[0], 16)
        msgs2.frame.data[1] = int(data2[1], 16)
        msgs2.frame.data[2] = int(data2[2], 16)
        msgs2.frame.data[3] = int(data2[3], 16)
        msgs2.frame.data[4] = int(data2[4], 16)
        msgs2.frame.data[5] = int(data2[5], 16)
        msgs2.frame.data[6] = int(data2[6], 16)
        msgs2.frame.data[7] = int(data2[7], 16)
    while True:
        ret2 = zcanlib.TransmitFD(chn_handle, msgs2, transmit_num2)

def run_0x345_lock():
    transmit_num5 = 1
    msgs5 = test_CanSend.ZCAN_TransmitFD_Data()
    for i in range(transmit_num5):
        msgs5.transmit_type = 0
        msgs5.frame.eff = 0
        msgs5.frame.rtr = 0
        msgs5.frame.can_id = int('345', 16)
        msgs5.frame.len = 16
        str5 = "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
        data5 = str5.split(' ')
        msgs5.frame.data[0] = int(data5[0], 16)
        msgs5.frame.data[1] = int(data5[1], 16)
        msgs5.frame.data[2] = int(data5[2], 16)
        msgs5.frame.data[3] = int(data5[3], 16)
        msgs5.frame.data[4] = int(data5[4], 16)
        msgs5.frame.data[5] = int(data5[5], 16)
        msgs5.frame.data[6] = int(data5[6], 16)
        msgs5.frame.data[7] = int(data5[7], 16)
        msgs5.frame.data[8] = int(data5[8], 16)
        msgs5.frame.data[9] = int(data5[9], 16)
        msgs5.frame.data[10] = int(data5[10], 16)
        msgs5.frame.data[11] = int(data5[11], 16)
        msgs5.frame.data[12] = int(data5[12], 16)
        msgs5.frame.data[13] = int(data5[13], 16)
        msgs5.frame.data[14] = int(data5[14], 16)
        msgs5.frame.data[15] = int(data5[15], 16)
    while True:
        ret5 = zcanlib.TransmitFD(chn_handle, msgs5, transmit_num5)

def run_0x319_Close():
    transmit_num6 = 1
    msgs6 = test_CanSend.ZCAN_TransmitFD_Data()
    for i in range(transmit_num6):
        msgs6.transmit_type = 0
        msgs6.frame.eff = 0
        msgs6.frame.rtr = 0
        msgs6.frame.can_id = int('319', 16)
        msgs6.frame.len = 16
        str6 = "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
        data6 = str6.split(' ')
        msgs6.frame.data[0] = int(data6[0], 16)
        msgs6.frame.data[1] = int(data6[1], 16)
        msgs6.frame.data[2] = int(data6[2], 16)
        msgs6.frame.data[3] = int(data6[3], 16)
        msgs6.frame.data[4] = int(data6[4], 16)
        msgs6.frame.data[5] = int(data6[5], 16)
        msgs6.frame.data[6] = int(data6[6], 16)
        msgs6.frame.data[7] = int(data6[7], 16)
        msgs6.frame.data[8] = int(data6[8], 16)
        msgs6.frame.data[9] = int(data6[9], 16)
        msgs6.frame.data[10] = int(data6[10], 16)
        msgs6.frame.data[11] = int(data6[11], 16)
        msgs6.frame.data[12] = int(data6[12], 16)
        msgs6.frame.data[13] = int(data6[13], 16)
        msgs6.frame.data[14] = int(data6[14], 16)
        msgs6.frame.data[15] = int(data6[15], 16)
    while True:
        ret6 = zcanlib.TransmitFD(chn_handle, msgs6, transmit_num6)

def run_0x295_off():
    transmit_num7 = 1
    msgs7 = test_CanSend.ZCAN_TransmitFD_Data()
    for i in range(transmit_num7):
        msgs7.transmit_type = 0
        msgs7.frame.eff = 0
        msgs7.frame.rtr = 0
        msgs7.frame.can_id = int('295', 16)
        msgs7.frame.len = 8
        str7 = "00 20 00 00 00 00 00 00"
        data7 = str7.split(' ')
        msgs7.frame.data[0] = int(data7[0], 16)
        msgs7.frame.data[1] = int(data7[1], 16)
        msgs7.frame.data[2] = int(data7[2], 16)
        msgs7.frame.data[3] = int(data7[3], 16)
        msgs7.frame.data[4] = int(data7[4], 16)
        msgs7.frame.data[5] = int(data7[5], 16)
        msgs7.frame.data[6] = int(data7[6], 16)
        msgs7.frame.data[7] = int(data7[7], 16)
    while True:
        ret7 = zcanlib.TransmitFD(chn_handle, msgs7, transmit_num7)

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


def ign_off():
    thread1 = threading.Thread(target=run_0x295_off)
    time.sleep(1)
    thread2 = threading.Thread(target=run_0x501)
    thread3 = threading.Thread(target=run_0x345_lock)
    time.sleep(1)
    thread4 = threading.Thread(target=run_0x319_Close)
    time.sleep(1)
    thread1.setDaemon(True)
    thread1.start()
    thread2.setDaemon(True)
    thread2.start()
    thread3.setDaemon(True)
    thread3.start()
    thread4.setDaemon(True)
    thread4.start()
#
if __name__ == "__main__":
    Ign_on.ign_on()
