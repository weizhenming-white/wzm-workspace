#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

# os.system("python ident.py --config_file /home/holo/bags/weima3 --show 1")


def test_bag(path):
    """
    测试bag是否ready
    """
    bag_list = list()
    print os.listdir(path)
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        # print file_path
        # print os.path.splitext(file_path)
        if os.path.splitext(file_path)[1] == ".bag":
            bag_list.append(file_path)

    print bag_list


if __name__ == '__main__':
    path = '/home/holo/bags/20200708_mogatan'
    test_bag(path)
