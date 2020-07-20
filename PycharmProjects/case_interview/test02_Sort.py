# -*- coding:utf-8 -*-

"""
Author:魏振明
time:2020-07-14 13:11
brief:通过不同的排序方式实现列表的排序
"""

def Bubbing(x):                             # x类型为列表
    """
    冒泡排序，比较两个相邻的元素，将值大的元素交换到右边
    """
    for i in range(len(x)):
        for j in range(len(x) - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
        print(x)
    
    return x

def Choice(x):
    """
    选择排序：每一次遍历待排序的序列，记录最小（大）值的下标，
    和待排序第一个元素进行比较，如果小（大）与待排序第一个元素，交换
    """
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]

    return x


if __name__ == "__main__":
    x = [10,1,35,61,89,36,55]
    # print(Choice(x))
    Bubbing(x)