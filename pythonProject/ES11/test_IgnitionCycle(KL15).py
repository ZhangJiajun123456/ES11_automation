"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/8 9:50
@Author  : Zhang jiajun
@Github  :
@Software: PyCharm
@File    : test_IgnitionCycle.py
休眠唤醒测试（KL15）
操作步骤：
1) KL15 on
2) 等待60s
3) KL15 off
4) 等待60s
5) 循环上述操作1000次
"""

import time
from ctypes import *
import platform
import ctypes
import threading
import inspect
import test_CanSend


def __run_0x295_on():
    transmit_num1 = 1
    msgs1 = test_CanSend.ZCAN_TransmitFD_Data()
    for i in range(transmit_num1):
        msgs1.transmit_type = 0
        msgs1.frame.eff = 0
        msgs1.frame.rtr = 0
        msgs1.frame.can_id = int('295', 16)
        msgs1.frame.len = 8
        str1 = "00 A0 00 00 00 00 00 00"
        data1 = str1.split(' ')
        msgs1.frame.data[0] = int(data1[0], 16)
        msgs1.frame.data[1] = int(data1[1], 16)
        msgs1.frame.data[2] = int(data1[2], 16)
        msgs1.frame.data[3] = int(data1[3], 16)
        msgs1.frame.data[4] = int(data1[4], 16)
        msgs1.frame.data[5] = int(data1[5], 16)
        msgs1.frame.data[6] = int(data1[6], 16)
        msgs1.frame.data[7] = int(data1[7], 16)
    while True:
        ret1 = zcanlib.TransmitFD(chn_handle, msgs1, transmit_num1)


def __run_0x501():
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


def __run_0x345_Unlock():
    transmit_num3 = 1
    msgs3 = test_CanSend.ZCAN_TransmitFD_Data()
    for i in range(transmit_num3):
        msgs3.transmit_type = 0
        msgs3.frame.eff = 0
        msgs3.frame.rtr = 0
        msgs3.frame.can_id = int('345', 16)
        msgs3.frame.len = 16
        str3 = "00 00 00 00 04 00 00 00 00 00 00 00 00 00 00 00"
        data3 = str3.split(' ')
        msgs3.frame.data[0] = int(data3[0], 16)
        msgs3.frame.data[1] = int(data3[1], 16)
        msgs3.frame.data[2] = int(data3[2], 16)
        msgs3.frame.data[3] = int(data3[3], 16)
        msgs3.frame.data[4] = int(data3[4], 16)
        msgs3.frame.data[5] = int(data3[5], 16)
        msgs3.frame.data[6] = int(data3[6], 16)
        msgs3.frame.data[7] = int(data3[7], 16)
        msgs3.frame.data[8] = int(data3[8], 16)
        msgs3.frame.data[9] = int(data3[9], 16)
        msgs3.frame.data[10] = int(data3[10], 16)
        msgs3.frame.data[11] = int(data3[11], 16)
        msgs3.frame.data[12] = int(data3[12], 16)
        msgs3.frame.data[13] = int(data3[13], 16)
        msgs3.frame.data[14] = int(data3[14], 16)
        msgs3.frame.data[15] = int(data3[15], 16)
    while True:
        ret3 = zcanlib.TransmitFD(chn_handle, msgs3, transmit_num3)


def __run_0x319_Open():
    transmit_num4 = 1
    msgs4 = test_CanSend.ZCAN_TransmitFD_Data()
    for i in range(transmit_num4):
        msgs4.transmit_type = 0
        msgs4.frame.eff = 0
        msgs4.frame.rtr = 0
        msgs4.frame.can_id = int('319', 16)
        msgs4.frame.len = 16
        str4 = "00 00 40 00 00 00 00 00 00 00 00 00 00 00 00 00"
        data4 = str4.split(' ')
        msgs4.frame.data[0] = int(data4[0], 16)
        msgs4.frame.data[1] = int(data4[1], 16)
        msgs4.frame.data[2] = int(data4[2], 16)
        msgs4.frame.data[3] = int(data4[3], 16)
        msgs4.frame.data[4] = int(data4[4], 16)
        msgs4.frame.data[5] = int(data4[5], 16)
        msgs4.frame.data[6] = int(data4[6], 16)
        msgs4.frame.data[7] = int(data4[7], 16)
        msgs4.frame.data[8] = int(data4[8], 16)
        msgs4.frame.data[9] = int(data4[9], 16)
        msgs4.frame.data[10] = int(data4[10], 16)
        msgs4.frame.data[11] = int(data4[11], 16)
        msgs4.frame.data[12] = int(data4[12], 16)
        msgs4.frame.data[13] = int(data4[13], 16)
        msgs4.frame.data[14] = int(data4[14], 16)
        msgs4.frame.data[15] = int(data4[15], 16)
    while True:
        ret4 = zcanlib.TransmitFD(chn_handle, msgs4, transmit_num4)


def __run_0x345_lock():
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


def __run_0x319_Close():
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


def __run_0x295_off():
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

if __name__ == "__main__":

    zcanlib = test_CanSend.ZCAN()
    handle = zcanlib.OpenDevice(test_CanSend.ZCAN_USBCANFD_200U, 0, 0)
    if handle == test_CanSend.INVALID_DEVICE_HANDLE:
        print("Open Device failed!")
        exit(0)
    print("device handle:%d." % (handle))

    info = zcanlib.GetDeviceInf(handle)
    print("Device Information:\n%s" % (info))
    #
    # Start CAN
    chn_handle = test_CanSend.can_start(zcanlib, handle, 0)
    print("channel handle:%d." % (chn_handle))
    for i in range(1000):
        #Send Can Message
        thread1 = threading.Thread(target=__run_0x295_on)
        thread2 = threading.Thread(target=__run_0x501)
        thread3 = threading.Thread(target=__run_0x345_Unlock)
        thread4 = threading.Thread(target=__run_0x319_Open)
        #启动线程
        thread1.setDaemon(True)
        thread1.start()
        thread2.setDaemon(True)
        thread2.start()
        thread3.setDaemon(True)
        thread3.start()
        thread4.setDaemon(True)
        thread4.start()
        time.sleep(30)
        #关闭线程
        stop_thread(thread1)
        stop_thread(thread2)
        stop_thread(thread3)
        stop_thread(thread4)


        # # 启动线程
        thread1 = threading.Thread(target=__run_0x295_off)
        time.sleep(1)
        thread2 = threading.Thread(target=__run_0x501)
        thread3 = threading.Thread(target=__run_0x345_lock)
        time.sleep(1)
        thread4 = threading.Thread(target=__run_0x319_Close)
        time.sleep(1)
        thread1.setDaemon(True)
        thread1.start()
        thread2.setDaemon(True)
        thread2.start()
        thread3.setDaemon(True)
        thread3.start()
        thread4.setDaemon(True)
        thread4.start()
        time.sleep(30)
        stop_thread(thread1)
        stop_thread(thread2)
        stop_thread(thread3)
        stop_thread(thread4)
        time.sleep(60)
        print('时间到，成功关闭信号发送')
    # Close CAN
    zcanlib.ResetCAN(chn_handle)
    # Close Device
    zcanlib.CloseDevice(handle)
    print('成功关闭周立功')


    # # Receive Messages
    # while True:
    #     rcv_num = zcanlib.GetReceiveNum(chn_handle, ZCAN_TYPE_CAN)
    #     print('adfs')
    #     rcv_canfd_num = zcanlib.GetReceiveNum(chn_handle, ZCAN_TYPE_CANFD)
    #     if rcv_num:
    #         print(rcv_num)
    #         print("Receive CAN message number:%d" % rcv_num)
    #         rcv_msg, rcv_num = zcanlib.Receive(chn_handle, rcv_num)
    #         for i in range(rcv_num):
    #             print("[%d]:ts:%d, id:%d, dlc:%d, eff:%d, rtr:%d, data:%s" % (i, rcv_msg[i].timestamp,
    #                                                                           rcv_msg[i].frame.can_id,
    #                                                                           rcv_msg[i].frame.can_dlc,
    #                                                                           rcv_msg[i].frame.eff,
    #                                                                           rcv_msg[i].frame.rtr,
    #                                                                           ''.join(
    #                                                                               str(rcv_msg[i].frame.data[j]) + ' '
    #                                                                               for j in
    #                                                                               range(rcv_msg[i].frame.can_dlc))))
    #     elif rcv_canfd_num:
    #         print('tttt')
    #         print("Receive CANFD message number:%d" % rcv_canfd_num)
    #         rcv_canfd_msgs, rcv_canfd_num = zcanlib.ReceiveFD(chn_handle, rcv_canfd_num, 1000)
    #         for i in range(rcv_canfd_num):
    #             print("[%d]:ts:%d, id:%d, len:%d, eff:%d, rtr:%d, esi:%d, brs: %d, data:%s" % (
    #                 i, rcv_canfd_msgs[i].timestamp, rcv_canfd_msgs[i].frame.can_id, rcv_canfd_msgs[i].frame.len,
    #                 rcv_canfd_msgs[i].frame.eff, rcv_canfd_msgs[i].frame.rtr,
    #                 rcv_canfd_msgs[i].frame.esi, rcv_canfd_msgs[i].frame.brs,
    #                 ''.join(str(rcv_canfd_msgs[i].frame.data[j]) + ' ' for j in range(rcv_canfd_msgs[i].frame.len))))
    #     else:
    #         break
    # #
