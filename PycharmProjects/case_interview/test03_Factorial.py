# -*- coding:utf-8 -*-

"""
Author:魏振明
time:2020-07-27 17:32
brief:输入一个数字，判断这个数字的阶乘
"""

def Factorial(x):
    if isinstance(x, int) or isinstance(x, float):
        if x == 0 or x == 1:
            return 1
        elif x > 1:
            sum = 1
            for i in range(2, int(x) + 1):
                sum = sum * i
            return sum
        else:
            return "The number entered needs to be greater than 0"
    else:
        return "Please re-enter an integer"

if __name__ == "__main__":
    print Factorial(20)