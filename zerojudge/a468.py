#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:57 2020

@author: fdbfvuie
"""

import calendar
n = int(input())
s = e = 0
for i in range(n):
    a, b, c = map(str, input().split())
    if a == "January" or a == "February":
        s = int(c)
    else:
        s = int(c) + 1
    a, b, c = map(str, input().split())
    if a == "January" or a == "February" and int(b[:-1]) < 29:
        e = int(c) - 1
    else:
        e = int(c)
    print("Case {}: {}".format(str(i+1), str(calendar.leapdays(s, e+1))))