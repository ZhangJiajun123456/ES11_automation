"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022\8\24 11:38
@Author  : starnight_cyber
@Github  : https:\\github.com\starnightcyber
@Software: PyCharm
@File    : test_123.py
"""
import os
from Common import common


vehicle = "1234567"
phone  = "3TG0221820007792"
device = common.Test(vehicle,phone)


def run():
    os.system('adb -s 1234567 shell am start com.beantechs.mediacenter/.ui.LaunchActivity')





if __name__ == "__main__":
    # table = xlrd2.open_workbook('D:\can.xlsx')
    # table = table.sheets()[0]
    # n_cols = table.ncols
    # print(n_cols)
    # cols_data = table.col_values(0,start_rowx=2,end_rowx=None)
    # print(cols_data)
    # device.d1.screenshot(r'D:\ES11\ES11_automation\TestPicture\01.png')
    # img1 = r'D:\ES11\ES11_automation\TestPicture\01.png' # 指定图片路径
    # img2 = r'D:\ES11\ES11_automation\TestPicture\12.png'
    # result = sc.image_contrast(img1,img2)
    # print(result)
    # if result == 0.0:
    #     print('pass')
    # else:
    #     print('false')
    # img = Image.open()
    # img_new = img.crop((720,1980,792,2052)).save(r'D:\ES11\ES11_automation\TestPicture\13.png')
    # sc.screenshot('01.png',((956,544,1092,680)),'01.png')
    # res = sc.image_contrast('01.png','12.png')
    # print(res)
    # print(os.getcwd())
    # img = 'D:\ES11\ES11_automation\TestPicture\\' + "01.png"
    # img = img + "01.png"
    # print(img)
    # device.play_BTmusic()
    # res = device.d2(resourceId="com.android.settings:id/switch_widget").info
    # print(res['checked'])
    # device.call_vehicleside('10086')
    # info = device.d1.xpath('//*[@resource-id="com.beantechs.btphone:id/tv_title_content"]').info
    # info = info['text']
    # if 'Click to Enter' in info:
    #     print(info)
    #     print(True)
    # info = device.d1.xpath('//*[@resource-id="com.beantechs.settings:id/sw_daynight"]/android.view.View[1]').info
    # print(info)
    # i = 5.6
    # print(int(i))
    # sc.image_contrast('ign_on.png','1.png')
    # sc.screenshot()
    run()