#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:43 2020

@author: fdbfvuie
"""

import datetime

n = int(input())
a, b = map(int, input().split())
t = datetime.datetime(2020, 1, 1, a, b)
c = []
for i in range(n):
    m = int(input())
    t = t + datetime.timedelta(minutes=m)
    c.append(t.strftime("%H:%M"))
d = [int(i) for i in input().split()]
for i in d:
    if i == 0:
        break
    print(c[i-1])