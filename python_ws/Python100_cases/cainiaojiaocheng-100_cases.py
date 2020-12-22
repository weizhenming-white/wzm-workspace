#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2020-10-11 20:59
brief:100道python练习题
"""
import math


def case_01():
    """
    题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
    程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
    """
    data = [1, 2, 3, 4]
    count = 0
    for a in data:
        for b in data:
            if b != a:
                for c in data:
                    if a != b and b != c and c != a:
                        print int(str(a) + str(b) + str(c))
                        count += 1
    print "Total is ", count


def case_02():
    """
    题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
         低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，
         可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，
         可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
    程序分析：请利用数轴来分界，定位。
    """
    profit = input("Please input the profit of the current month(Unit: ten thousand): ")
    if profit <= 10:
        total_bonus = profit * 0.1
        print "The total amount of bonus to be paid is: ", total_bonus
    elif 10 < profit <= 20:
        total_bonus = ((profit - 10) * 0.075) + (10 * 0.1)
        print "The total amount of bonus to be paid is: ", total_bonus
    elif 20 < profit <= 40:
        total_bonus = ((profit - 20) * 0.05) + (10 * 0.1) + (10 * 0.75)
        print "The total amount of bonus to be paid is: ", total_bonus
    elif 40 < profit <= 60:
        total_bonus = ((profit - 40) * 0.03) + (10 * 0.1) + (10 * 0.75) + (20 * 0.05)
        print "The total amount of bonus to be paid is: ", total_bonus
    elif 60 < profit <= 100:
        total_bonus = ((profit - 60) * 0.015) + (10 * 0.1) + (10 * 0.75) + (20 * 0.05) + (20 * 0.03)
        print "The total amount of bonus to be paid is: ", total_bonus
    else:
        total_bonus = ((profit - 100) * 0.01) + (10 * 0.1) + (10 * 0.75) + (20 * 0.05) + (20 * 0.03) + (40 * 0.015)
        print "The total amount of bonus to be paid is: ", total_bonus
    """
    # 菜鸟教程上的例子，比较简单，通过将不同区间的利润关联起来，进而得出奖金总数
    i = int(raw_input('净利润:'))
    arr = [1000000,600000,400000,200000,100000,0]
    rat = [0.01,0.015,0.03,0.05,0.075,0.1]
    r = 0
    for idx in range(0,6):
        if i>arr[idx]:
            r+=(i-arr[idx])*rat[idx]
            print (i-arr[idx])*rat[idx]
            i=arr[idx]
    print r
    """


def case_03():
    """
    题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
    程序分析：
    假设该数为 x。
    1、则：x + 100 = n2, x + 100 + 168 = m2
    2、计算等式：m2 - n2 = (m + n)(m - n) = 168
    3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
    4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
    5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
    6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
    7、接下来将 i 的所有数字循环计算即可。
    """
    for i in range(1, 85):
        if 168 % i == 0:
            j = 168 / i
            if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
                m = (i + j) / 2
                n = (i - j) / 2
                x = n * n - 100
                print(x)


def case_04():
    """
    题目：输入某年某月某日，判断这一天是这一年的第几天？
    程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
    闰年判断方法：普通闰年：公历年份是4的倍数的，且不是100的倍数，为普通闰年（如2004年、2020年就是闰年）。
                世纪闰年：公历年份是整百数的，必须是400的倍数才是世纪闰年（如1900年不是世纪闰年，2000年是世纪闰年）。
    """
    year = input("year: \n")
    month = input("month: \n")
    day = input("day: \n")

    sum = 0
    months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
    if 0 < month <= 12:
        sum = months[month - 1]
    else:
        print 'data error'
    sum += day
    leap = 0
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        leap = 1
    if (leap == 1) and (month > 2):
        sum += 1
    print 'it is the %dth day.' % sum


if __name__ == '__main__':
    case_04()
