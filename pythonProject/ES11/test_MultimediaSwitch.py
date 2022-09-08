
"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2022/8/24 14:16
@Author  : zhangjiajun
@Github  :
@Software: PyCharm
@File    : test_MultimediaSwitch.py
多媒体点击测试
操作步骤：
   1) 音乐播放，上一曲/下一曲/暂定/播放，进入播放列表，随机播放一首，关闭播放列表。
   2) 视频播放，上一视频/下一视频/暂定/播放。
   3) 上述步骤交互进行12个小时
"""

import os
import time
import uiautomator2 as u2

d =u2.connect("1234567")
class Test:
    def test_run(self):
        try:
            while True:
                os.system("adb -s 1234567 shell am start com.beantechs.mediacenter/com.beantechs.mediacenter.ui.HomeActivity")     #进入多媒体画面
                time.sleep(1)
                d.xpath(
                    '//*[@resource-id="com.beantechs.mediacenter:id/tab_usb_music"]/android.widget.FrameLayout[1]').click()     #点击USB音乐
                time.sleep(1)
                d.xpath('//*[@resource-id="com.beantechs.mediacenter:id/next"]').click()        #点击next button
                time.sleep(1)
                d.xpath('//*[@resource-id="com.beantechs.mediacenter:id/prev"]').click()        #点击pre button
                time.sleep(1)
                for i in range(2):
                    d.xpath('//*[@resource-id="com.beantechs.mediacenter:id/play_pause"]').click()      #点击pause/play button
                    time.sleep(1)
                d.xpath('//*[@resource-id="com.beantechs.mediacenter:id/toggle"]').click()          #点击列表button
                time.sleep(1)
                #随机选择歌曲播放
                d.xpath(
                    '//*[@resource-id="com.beantechs.mediacenter:id/music_list"]/android.widget.RelativeLayout[4]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').click()
                time.sleep(3)
                d.xpath(
                    '//*[@resource-id="com.beantechs.mediacenter:id/tab_local_video"]/android.widget.FrameLayout[1]').click()   #点击video button
                time.sleep(1)
                #点击视频播放
                d.xpath(
                    '//*[@resource-id="com.beantechs.mediacenter:id/recycle"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
                time.sleep(1)
                #通过坐标点击next button
                d.click(337, 598)
                time.sleep(1)
                #通过坐标点击play/pause button
                for i in range(2):
                    d.click(237, 598)
                    time.sleep(1)
        except Exception as result:
            print(result)
        finally:
            Test().test_run()

if __name__ == "__main__":
    Test().test_run()
