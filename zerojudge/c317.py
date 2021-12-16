#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:14 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    x, a, b = map(int, input().split())
    c = x // a
    d = 1
    for j in range(c, -1, -1):
        if (x - j * a) % b == 0:
            print(int(j + (x - j*a) / b))
            d = 0
            break
    if d:
        print("-1")