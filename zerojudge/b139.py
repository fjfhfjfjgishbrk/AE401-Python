#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 7 12:19 2020

@author: fdbfvuie
"""

b, n = map(int, input().split())
a = []
la = []
ra = []
t = []
for i in range(n):
    l, r = map(int, input().split())
    la.append(l)
    ra.append(r)
t = la.copy() + ra.copy()
t.sort()
c = 0
temp = 0
for i in t:
    if c == 0:
        if i in la:
            c += 1
            temp = i
    else:
        if i in la and i in ra:
            continue
        elif i in la:
            c += 1
        else:
            c -= 1
            if c == 0:
                a.append([temp, i])
length = 0
for i in a:
    length += abs(i[1] - i[0]) + 1
print(b - length + 1)