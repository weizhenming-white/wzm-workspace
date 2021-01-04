#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2020-11-25 16:51
brief: opencv读取视频流
"""

import cv2
import numpy
import sys

def video_to_image():
    # path = '/home/holo/bags/20201112/holo_stream_F_20201030120919_0_321.h264'
    path = '/home/holo/bags/20201116/holo_stream_F_20201030120722_0_424.h264'
    cap = cv2.VideoCapture(path)  # 调整参数实现读取视频或调用摄像头

    isOpened = cap.isOpened()
    fps = cap.get(cv2.CAP_PROP_FPS)  ##获取帧率
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  ###获取宽度
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  ###获取高度
    print(fps, width, height)

    print(isOpened)

    i = 0
    while True:
        ret, frame = cap.read()  # 读取
        filename = 'image' + str(i) + '.jpg'
        # print(filename)
        print(ret)
        i = i + 1
        if ret:
            cv2.imshow("cap", frame)  # 显示
            cv2.imwrite("./%s" % filename, frame, [cv2.IMWRITE_JPEG_CHROMA_QUALITY, 100])  # 命名 图片 图片质量)
            img = cv2.imread(filename)
            img1 = img[0:480, 0:640]
            cv2.imwrite('%s.jpg' % i, img1)
        else:
            break

        if cv2.waitKey(1) & 0xff == ord('q'):  # 按q退出
            break
    cap.release()
    cv2.destroyAllWindows()

def crop_image():
    image_path = 'image0.jpg'
    img = cv2.imread(image_path)   # 读入一副图片
    img1 = img[0:480, 0:640] #需要保留的区域--裁剪 参数1 是高度的范围，参数2是宽度的范围
    cv2.imwrite('1.jpg', img1)

    # 使用函数cv2.flip(img,flipcode)翻转图像，flipcode控制翻转效果。
    # flipcode = 0：沿x轴翻转;flipcode > 0：沿y轴翻转;flipcode < 0：x,y轴同时翻转
    imgflip = cv2.flip(img1, -1)

    # 彩色图像转为灰度图像
    img2 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)

    # 灰度图像转为伪彩色图像
    image_np = cv2.applyColorMap(img2, cv2.COLORMAP_OCEAN)
    # 原图伪彩色
    image_np1 = cv2.applyColorMap(img1, cv2.COLORMAP_OCEAN)
    # 对于伪彩图有不同的伪彩图方式，各个函数如下：
    # COLORMAP_AUTUMN = 0,
    # COLORMAP_BONE = 1,
    # COLORMAP_JET = 2,
    # COLORMAP_WINTER = 3,
    # COLORMAP_RAINBOW = 4,
    # COLORMAP_OCEAN = 5,
    # COLORMAP_SUMMER = 6,
    # COLORMAP_SPRING = 7,
    # COLORMAP_COOL = 8,
    # COLORMAP_HSV = 9,
    # COLORMAP_PINK = 10,
    # COLORMAP_HOT = 11

    # 修改图像分辨率
    img_new = cv2.resize(img1, (1280, 728))

    cv2.imshow("src", img1)
    # cv2.imshow("gray", img2)
    # cv2.imshow("output", image_np)
    # cv2.imshow("result", image_np1)
    cv2.imshow("img_new", img_new)
    cv2.waitKey(0)

if __name__ == '__main__':
    crop_image()
    # video_to_image()