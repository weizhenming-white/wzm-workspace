#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author:魏振明
time:2020-07-29 16:06
brief:随机数练习，给出1-100之间的一个数字，然后看看花了几次猜对
"""

import random

answer = random.randint(1, 100)
counter = 0
while True:

    counter += 1
    tmp = int(input("Please enter an integer between 1 and 100: "))
    if tmp == answer:
        print("Congratulations, that's right")
        break
    elif tmp > answer:
        print("Sorry, it's too big")
    elif tmp < answer:
        print("Sorry, it's too small")

print("你总共猜了%d次" % counter)
