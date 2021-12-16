#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 7 10:46 2020

@author: fdbfvuie
"""

a, b = map(int, input().split())
c = a // 12
if c >= b:
    print(b)
else:
    a = a % 12 + 2 * c
    b -= c
    while a >= 12 and b > 0:
        c += 1
        a -= 10
        b -= 1
    while (a + b) > 12 and b > 0:
        b -= (12 - a)
        c += 1
        a = 2
        b -= 1
    print(c)