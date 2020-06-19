#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 19:12 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    a = [int(i) for i in input().split()]
    a.sort()
    s = len(a) * (a[0] + a[-1]) / 2
    for j in a:
        if a.count(j) > 1:
            repeat = j
            break
    miss = int(repeat + s - sum(a))
    print("{} {}".format(miss, repeat))