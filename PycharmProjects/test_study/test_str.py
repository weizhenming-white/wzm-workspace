#!/usr/bin/env python
# -*- coding:utf-8 -*-

str1 = "13811530991@163.com"

data = dict()
for i in str1:
    data[i] = int(str1.count(i))

for i in range(0, len(data.keys()) - 1):
    for j in range(i + 1, len(data.keys)):
        pass





















# test1 = list()
# str2 = str()
# for i in str1:
#     if i not in str2:
#         test1.append(int(str1.count(i)))
#         str2 += i

# test1.sort()

# for i in str2:
#     if test1[len(test1) - 1] >= int(str1.count(i)) >= test1[len(test1) - 3]:
#         print "need element is ", i, "  and this element appear ", str1.count(i)

    