"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/09/07 15:02:07
@Author  : zhangjiajun
@Github  : git@github.com:ZhangJiajun123456/ES11_automation.git
@Software: PyCharm
@File    : CanMessage.py
"""
import test_CanSend
import threading
import time
import xlrd2

class Test():
    def driver(self):
        global chn_handle
        global zcanlib
        global handle
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

    def close_zcanpro(self):
        # Close CAN
        zcanlib.ResetCAN(chn_handle)
        # Close Device
        zcanlib.CloseDevice(handle)
        print('成功关闭周立功')

    def run_0x295_on(self):
        transmit_num = 1
        msgs = test_CanSend.ZCAN_TransmitFD_Data()
        for i in range(transmit_num):
            msgs.transmit_type = 0
            msgs.frame.eff = 0
            msgs.frame.rtr = 0
            msgs.frame.can_id = int('295', 16)
            msgs.frame.len = 8
            str = "00 A0 00 00 00 00 00 00"
            data = str.split(' ')
            msgs.frame.data[0] = int(data[0], 16)
            msgs.frame.data[1] = int(data[1], 16)
            msgs.frame.data[2] = int(data[2], 16)
            msgs.frame.data[3] = int(data[3], 16)
            msgs.frame.data[4] = int(data[4], 16)
            msgs.frame.data[5] = int(data[5], 16)
            msgs.frame.data[6] = int(data[6], 16)
            msgs.frame.data[7] = int(data[7], 16)
        while True:
            ret = zcanlib.TransmitFD(chn_handle, msgs, transmit_num)

    def run_0x501(self):
        transmit_num = 1
        msgs = test_CanSend.ZCAN_TransmitFD_Data()
        for i in range(transmit_num):
            msgs.transmit_type = 0
            msgs.frame.eff = 0
            msgs.frame.rtr = 0
            msgs.frame.can_id = int('501', 16)
            msgs.frame.len = 8
            str = "00 00 00 00 00 00 00 00"
            data = str.split(' ')
            msgs.frame.data[0] = int(data[0], 16)
            msgs.frame.data[1] = int(data[1], 16)
            msgs.frame.data[2] = int(data[2], 16)
            msgs.frame.data[3] = int(data[3], 16)
            msgs.frame.data[4] = int(data[4], 16)
            msgs.frame.data[5] = int(data[5], 16)
            msgs.frame.data[6] = int(data[6], 16)
            msgs.frame.data[7] = int(data[7], 16)
        while True:
            ret = zcanlib.TransmitFD(chn_handle, msgs, transmit_num)


    def run_0x345_Unlock(self):
        transmit_num = 1
        msgs = test_CanSend.ZCAN_TransmitFD_Data()
        for i in range(transmit_num):
            msgs.transmit_type = 0
            msgs.frame.eff = 0
            msgs.frame.rtr = 0
            msgs.frame.can_id = int('345', 16)
            msgs.frame.len = 16
            str = "00 00 00 00 04 00 00 00 00 00 00 00 00 00 00 00"
            data = str.split(' ')
            msgs.frame.data[0] = int(data[0], 16)
            msgs.frame.data[1] = int(data[1], 16)
            msgs.frame.data[2] = int(data[2], 16)
            msgs.frame.data[3] = int(data[3], 16)
            msgs.frame.data[4] = int(data[4], 16)
            msgs.frame.data[5] = int(data[5], 16)
            msgs.frame.data[6] = int(data[6], 16)
            msgs.frame.data[7] = int(data[7], 16)
            msgs.frame.data[8] = int(data[8], 16)
            msgs.frame.data[9] = int(data[9], 16)
            msgs.frame.data[10] = int(data[10], 16)
            msgs.frame.data[11] = int(data[11], 16)
            msgs.frame.data[12] = int(data[12], 16)
            msgs.frame.data[13] = int(data[13], 16)
            msgs.frame.data[14] = int(data[14], 16)
            msgs.frame.data[15] = int(data[15], 16)
            ret = zcanlib.TransmitFD(chn_handle, msgs, transmit_num)


    def run_0x319_Open(self):
        transmit_num = 1
        msgs = test_CanSend.ZCAN_TransmitFD_Data()
        for i in range(transmit_num):
            msgs.transmit_type = 0
            msgs.frame.eff = 0
            msgs.frame.rtr = 0
            msgs.frame.can_id = int('319', 16)
            msgs.frame.len = 16
            str = "00 00 40 00 00 00 00 00 00 00 00 00 00 00 00 00"
            data = str.split(' ')
            msgs.frame.data[0] = int(data[0], 16)
            msgs.frame.data[1] = int(data[1], 16)
            msgs.frame.data[2] = int(data[2], 16)
            msgs.frame.data[3] = int(data[3], 16)
            msgs.frame.data[4] = int(data[4], 16)
            msgs.frame.data[5] = int(data[5], 16)
            msgs.frame.data[6] = int(data[6], 16)
            msgs.frame.data[7] = int(data[7], 16)
            msgs.frame.data[8] = int(data[8], 16)
            msgs.frame.data[9] = int(data[9], 16)
            msgs.frame.data[10] = int(data[10], 16)
            msgs.frame.data[11] = int(data[11], 16)
            msgs.frame.data[12] = int(data[12], 16)
            msgs.frame.data[13] = int(data[13], 16)
            msgs.frame.data[14] = int(data[14], 16)
            msgs.frame.data[15] = int(data[15], 16)
            ret = zcanlib.TransmitFD(chn_handle, msgs, transmit_num)


    def run_0x345_lock(self):
        transmit_num = 1
        msgs = test_CanSend.ZCAN_TransmitFD_Data()
        for i in range(transmit_num):
            msgs.transmit_type = 0
            msgs.frame.eff = 0
            msgs.frame.rtr = 0
            msgs.frame.can_id = int('345', 16)
            msgs.frame.len = 16
            str = "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
            data = str.split(' ')
            msgs.frame.data[0] = int(data[0], 16)
            msgs.frame.data[1] = int(data[1], 16)
            msgs.frame.data[2] = int(data[2], 16)
            msgs.frame.data[3] = int(data[3], 16)
            msgs.frame.data[4] = int(data[4], 16)
            msgs.frame.data[5] = int(data[5], 16)
            msgs.frame.data[6] = int(data[6], 16)
            msgs.frame.data[7] = int(data[7], 16)
            msgs.frame.data[8] = int(data[8], 16)
            msgs.frame.data[9] = int(data[9], 16)
            msgs.frame.data[10] = int(data[10], 16)
            msgs.frame.data[11] = int(data[11], 16)
            msgs.frame.data[12] = int(data[12], 16)
            msgs.frame.data[13] = int(data[13], 16)
            msgs.frame.data[14] = int(data[14], 16)
            msgs.frame.data[15] = int(data[15], 16)
            ret = zcanlib.TransmitFD(chn_handle, msgs, transmit_num)


    def run_0x319_Close(self):
        transmit_num = 1
        msgs = test_CanSend.ZCAN_TransmitFD_Data()
        for i in range(transmit_num):
            msgs.transmit_type = 0
            msgs.frame.eff = 0
            msgs.frame.rtr = 0
            msgs.frame.can_id = int('319', 16)
            msgs.frame.len = 16
            str = "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
            data = str.split(' ')
            msgs.frame.data[0] = int(data[0], 16)
            msgs.frame.data[1] = int(data[1], 16)
            msgs.frame.data[2] = int(data[2], 16)
            msgs.frame.data[3] = int(data[3], 16)
            msgs.frame.data[4] = int(data[4], 16)
            msgs.frame.data[5] = int(data[5], 16)
            msgs.frame.data[6] = int(data[6], 16)
            msgs.frame.data[7] = int(data[7], 16)
            msgs.frame.data[8] = int(data[8], 16)
            msgs.frame.data[9] = int(data[9], 16)
            msgs.frame.data[10] = int(data[10], 16)
            msgs.frame.data[11] = int(data[11], 16)
            msgs.frame.data[12] = int(data[12], 16)
            msgs.frame.data[13] = int(data[13], 16)
            msgs.frame.data[14] = int(data[14], 16)
            msgs.frame.data[15] = int(data[15], 16)
            ret = zcanlib.TransmitFD(chn_handle, msgs, transmit_num)


    def run_0x295_off(self):
        transmit_num = 1
        msgs = test_CanSend.ZCAN_TransmitFD_Data()
        for i in range(transmit_num):
            msgs.transmit_type = 0
            msgs.frame.eff = 0
            msgs.frame.rtr = 0
            msgs.frame.can_id = int('295', 16)
            msgs.frame.len = 8
            str = "00 20 00 00 00 00 00 00"
            data = str.split(' ')
            msgs.frame.data[0] = int(data[0], 16)
            msgs.frame.data[1] = int(data[1], 16)
            msgs.frame.data[2] = int(data[2], 16)
            msgs.frame.data[3] = int(data[3], 16)
            msgs.frame.data[4] = int(data[4], 16)
            msgs.frame.data[5] = int(data[5], 16)
            msgs.frame.data[6] = int(data[6], 16)
            msgs.frame.data[7] = int(data[7], 16)
        while True:
            ret = zcanlib.TransmitFD(chn_handle, msgs, transmit_num)

    def run_0x295_acc(self):
        transmit_num = 1
        msgs = test_CanSend.ZCAN_TransmitFD_Data()
        for i in range(transmit_num):
            msgs.transmit_type = 0
            msgs.frame.eff = 0
            msgs.frame.rtr = 0
            msgs.frame.can_id = int('295', 16)
            msgs.frame.len = 8
            str = "00 60 00 00 00 00 00 00"
            data = str.split(' ')
            msgs.frame.data[0] = int(data[0], 16)
            msgs.frame.data[1] = int(data[1], 16)
            msgs.frame.data[2] = int(data[2], 16)
            msgs.frame.data[3] = int(data[3], 16)
            msgs.frame.data[4] = int(data[4], 16)
            msgs.frame.data[5] = int(data[5], 16)
            msgs.frame.data[6] = int(data[6], 16)
            msgs.frame.data[7] = int(data[7], 16)
        while True:
            zcanlib.TransmitFD(chn_handle, msgs, transmit_num)

    def run_29F(self):
        transmit_num = 1
        msgs = test_CanSend.ZCAN_TransmitFD_Data()
        for i in range(transmit_num):
            msgs.transmit_type = 0
            msgs.frame.eff = 0
            msgs.frame.rtr = 0
            msgs.frame.can_id = int('29F', 16)
            msgs.frame.len = 8
            str = "00 01 00 00 00 00 00 00"
            data = str.split(' ')
            msgs.frame.data[0] = int(data[0], 16)
            msgs.frame.data[1] = int(data[1], 16)
            msgs.frame.data[2] = int(data[2], 16)
            msgs.frame.data[3] = int(data[3], 16)
            msgs.frame.data[4] = int(data[4], 16)
            msgs.frame.data[5] = int(data[5], 16)
            msgs.frame.data[6] = int(data[6], 16)
            msgs.frame.data[7] = int(data[7], 16)
            zcanlib.TransmitFD(chn_handle, msgs, transmit_num)

    #车速报文
    def run_137(self):
        transmit_num = 1
        msgs = test_CanSend.ZCAN_TransmitFD_Data()
        for i in range(transmit_num):
            msgs.transmit_type = 0
            msgs.frame.eff = 0
            msgs.frame.rtr = 0
            msgs.frame.can_id = int('137', 16)
            msgs.frame.len = 64
            str0 = "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 05 50 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 20 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
            str1 = "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 05 50 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 23 f5 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
            str2 = "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 05 50 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 27 fc 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
            str3 = "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 05 50 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 2c 0c 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
            str4 = "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 05 50 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 30 1c 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 "
            str = [str0,str1,str2,str3,str4]
            while True:
                for i in range(4):
                    data = str[i+1].split(' ')
                    for i in range(64):
                        msgs.frame.data[i] = int(data[i], 16)
                    for i in range(30):
                        zcanlib.TransmitFD(chn_handle, msgs, transmit_num)
                        time.sleep(0.05)
                for i in range(4):
                    data = str[3 - i].split(' ')
                    for i in range(64):
                        msgs.frame.data[i] = int(data[i], 16)
                    for i in range(30):
                        zcanlib.TransmitFD(chn_handle, msgs, transmit_num)
                        time.sleep(0.05)

    def run_0x244(self):
        while True:
            transmit_num = 1
            msgs = test_CanSend.ZCAN_TransmitFD_Data()
            for i in range(transmit_num):
                msgs.transmit_type = 0
                msgs.frame.eff = 0
                msgs.frame.rtr = 0
                msgs.frame.can_id = int('244', 16)
                msgs.frame.len = 8
                str0 = "00 40 00 00 00 00 00 00"
                str1 = "00 10 00 00 00 00 00 00"
                str2 = "00 04 00 00 00 00 00 00"
                str3 = "00 01 00 00 00 00 00 00"

                str = [str0, str1, str2, str3]
                for i in range(4):
                    data = str[i].split(' ')
                    for j in range(8):
                        msgs.frame.data[j] = int(data[j],16)
                    for k in range(5):
                        zcanlib.TransmitFD(chn_handle, msgs, transmit_num)
                        time.sleep(2)

    def run_0x2FB(self):
        transmit_num1 = 1
        msgs1 = test_CanSend.ZCAN_TransmitFD_Data()
        for i in range(transmit_num1):
            msgs1.transmit_type = 0
            msgs1.frame.eff = 0
            msgs1.frame.rtr = 0
            msgs1.frame.can_id = int('2FB', 16)
            msgs1.frame.len = 8
            str1 = "00 00 00 00 00 00 00 00"
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
            zcanlib.TransmitFD(chn_handle, msgs1, transmit_num1)
            time.sleep(0.05)

    def test_highload(self):
        can_len = []
        table = xlrd2.open_workbook('../信号梳理.xlsx')
        table = table.sheets()[0]
        # 遍历canid
        canid_data = table.col_values(0, start_rowx=2, end_rowx=406)
        canmsg_data = table.col_values(3, start_rowx=2, end_rowx=406)
        for i in range(len(canid_data)):
            if type(canid_data[i]) == float:
                canid_data[i] = int(canid_data[i])
        transmit_num = 1
        msgs = test_CanSend.ZCAN_TransmitFD_Data()
        while True:
            for i in range(len(canmsg_data)):
                msgs.transmit_type = 0
                msgs.frame.eff = 0
                msgs.frame.rtr = 0
                msgs.frame.can_id = int(str(canid_data[i]), 16)
                str1 = canmsg_data[i]
                data = str1.split(' ')
                msgs.frame.len = len(data)
                # 判断报文长度
                if len(data) == 8:
                    for j in range(8):
                        msgs.frame.data[j] = int(data[j], 16)
                elif len(data) == 16:
                    for j in range(16):
                        msgs.frame.data[j] = int(data[j], 16)
                else:
                    for j in range(64):
                        msgs.frame.data[j] = int(data[j], 16)
                time.sleep(0.5)
                zcanlib.TransmitFD(chn_handle, msgs, transmit_num)
                print(i)

    def test_chime(self):
        table = xlrd2.open_workbook('../信号梳理.xlsx')
        table = table.sheets()[0]
        # 遍历canid
        canid_data = table.col_values(0, start_rowx=205, end_rowx=406)
        canmsg_data = table.col_values(3, start_rowx=205, end_rowx=406)
        for i in range(len(canid_data)):
            if type(canid_data[i]) == float:
                canid_data[i] = int(canid_data[i])

        transmit_num = 1
        msgs = test_CanSend.ZCAN_TransmitFD_Data()
        while True:
            for i in range(len(canmsg_data)):
                msgs.transmit_type = 0
                msgs.frame.eff = 0
                msgs.frame.rtr = 0
                msgs.frame.can_id = int(str(canid_data[i]), 16)
                str1 = canmsg_data[i]
                data = str1.split(' ')
                msgs.frame.len = len(data)
                # 判断报文长度
                if len(data) == 8:
                    for j in range(8):
                        msgs.frame.data[j] = int(data[j], 16)
                elif len(data) == 16:
                    for j in range(16):
                        msgs.frame.data[j] = int(data[j], 16)
                else:
                    for j in range(64):
                        msgs.frame.data[j] = int(data[j], 16)

                zcanlib.TransmitFD(chn_handle, msgs, transmit_num)
                # time.sleep(0.5)
                print(i)

if __name__ == "__main__":
    Test().driver()
    thread2 = threading.Thread(target=Test().run_0x295_on)
    thread3 = threading.Thread(target=Test().run_0x501)
    time.sleep(2)
    thread2.start()
    thread3.start()
    # print(chn_handle)