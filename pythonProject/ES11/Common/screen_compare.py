"""
!/usrbin/env python
-*- coding: utf-8 -*-
@Time    : 2022\08\29 13:28:22
@Author  : zhangjiajun
@Github  : git@github.com:ZhangJiajun123456\ES11_automation.git
@Software: PyCharm
@File    : screen_compare.py
"""

from PIL import Image
import math
import operator
from functools import reduce


def image_contrast(pic_old,pic_new):
    img1 = 'D:/ES11/ES11_automation\image/' + pic_old
    img2 = 'D:/ES11/ES11_automation/TestPicture/' + pic_new
    image1 = Image.open(img1)
    image2 = Image.open(img2)
    h1 = image1.histogram()
    h2 = image2.histogram()
    result = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1))
    return result

#截取图片中的一部分
def screenshot(open_pic,box,save_path):
    open_pic = 'D:/ES11/ES11_automation/TestPicture/' + open_pic
    save_path = 'D:/ES11/ES11_automation/TestPicture/' + save_path
    img = Image.open(open_pic)
    img.crop(box).save(save_path)
