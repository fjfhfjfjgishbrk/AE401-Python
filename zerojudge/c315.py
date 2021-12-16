#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 10:13 2020

@author: fdbfvuie
"""

n = int(input())
x = y = 0
for i in range(n):
    a, b = map(int, input().split())
    if a == 0:
        y += b
    elif a == 1:
        x += b
    elif a == 2:
        y -= b
    elif a == 3:
        x -= b
print("{} {}".format(str(x), str(y)))