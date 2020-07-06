#!/usr/bin/env python
# -*- coding:utf-8 -*-

def parseTrigon(a, b, c):
    data = [a, b, c]
    for i in data:
        if 1 <= i <= 10:
            pass
        else:
            return -1
    for i in data:
        if ((a + b) <= c) or ((a + c) <= b) or ((b + c) <= a):
            return 0
        if (a != b) and (a != c) and (b != c):
            return 1
        if a == b == c:
            return 3
        if (a ==b) or (a == c) or (b ==c):
            return 2


if __name__ == "__main__":
    print parseTrigon(3, "3" , 6)