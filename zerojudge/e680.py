#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 11:19 2020

@author: fdbfvuie
"""

import datetime
n = int(input())
for i in range(n):
    b = input()
    c = datetime.datetime(int(b[4:]), int(b[:2]), int(b[2:4])) + datetime.timedelta(days=280)
    b = c.strftime("%m") + c.strftime("%d") + c.strftime("%Y")
    print("{} {}/{}/{} ".format(str(i+1), b[:2], b[2:4], b[4:]), end="")
    a = int(b[:4])
    if a < 121:
        print("capricorn")
    elif a < 220:
        print("aquarius")
    elif a < 321:
        print("pisces")
    elif a < 421:
        print("aries")
    elif a < 522:
        print("taurus")
    elif a < 622:
        print("gemini")
    elif a < 723:
        print("cancer")
    elif a < 822:
        print("leo")
    elif a < 924:
        print("virgo")
    elif a < 1024:
        print("libra")
    elif a < 1123:
        print("scorpio")
    elif a < 1223:
        print("sagittarius")
    else:
        print("capricorn")