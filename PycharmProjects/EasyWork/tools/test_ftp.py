#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2020-11-10 20:06
brief:学习自动连接ftp服务器，然后下载对应日期的bag
"""

import ftplib
import os
import sys


class FTPSync(object):
    """
    连接ftp，并操作
    """

    def __init__(self):
        # 设置变量
        self.ftp = ftplib.FTP()

    def login(self, host, port, username, passwd):
        # 连接ftp
        self.ftp.connect(host, port)
        # 登录ftp服务器
        self.ftp.login(username, passwd)
        self.ftp.set_pasv(False)      # true：允许被动模式，false：禁用被动模式。默认允许
        # 打印出欢迎消息
        print(self.ftp.getwelcome())

    def get_file(self, ftp_path, start_date, local_path):
        # print(ftp_path)
        path_list = []
        bag_list = []

        # print(self.ftp.nlst(ftp_path))
        # 获取文件夹下的文件名称列表，并筛选出这一周的数据目录
        for day in self.ftp.nlst(ftp_path):
            # 过滤出符合需要的文件夹目录
            if start_date <= int(os.path.basename(day)) <= start_date + 5:
                path_list.append(day)

        # 过滤出每个要处理bag的路径
        for path in path_list:
            for bag in self.ftp.nlst(path):
                if '.' in os.path.basename(bag):
                    if os.path.splitext(os.path.basename(bag))[1] == '.bag':
                        bag_list.append(bag)

        print(path_list)
        print(bag_list)
        # 下载对应的bag
        for item in bag_list:
            if not os.path.exists(os.path.join(local_path, os.path.basename(item))):
                print('\n===================================================================\n')
                print("Start download file ", os.path.basename(item))
                file_handler = open(os.path.join(local_path, os.path.basename(item)), 'wb')
                try:
                    self.ftp.retrbinary("RETR %s" % item, file_handler.write)  # 接收服务器上文件并写入本地文件
                except:
                    print('Failed to download file, Bag name is ', item)
                else:
                    print("Download file %s success!" % item)
                finally:
                    file_handler.close()
            else:
                print('\n%s file already exist.' % item)

    def close(self):
        # 退出ftp连接
        self.ftp.quit()


if __name__ == '__main__':
    ftp = FTPSync()
    ftp.login('ftp.holomatic.ai', 21, 'holo', '1709heduo')  # 主机，端口号，用户名，密码
    ftp.get_file('/Rosbag_parking/weltmeister', 20201109, '/home/holo/wzm_test')  # FTP路径，开始时间，本地存放bag的路径
    ftp.close()