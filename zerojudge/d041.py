#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:02 2020

@author: fdbfvuie
"""

import datetime
n = int(input())
for i in range(n):
    input()
    d1, m1, y1 = map(int, input().split("/"))
    d2, m2, y2 = map(int, input().split("/"))
    a = datetime.datetime(y1, m1, d1)
    b = datetime.datetime(y2, m2, d2)
    c = b - a
    if c.days > 0:
        print("Case #{}: Invalid birth date".format(i + 1))
    else:
        if (datetime.datetime(2000, m1, d1) - datetime.datetime(2000, m2, d2)).days < 0:
            age = y1 - y2 - 1
        else:
            age = y1 - y2
        if age > 130:
            print("Case #{}: Check birth date".format(i + 1))
        else:
            print("Case #{}: {}".format(i + 1, age))