#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 10:15 2020

@author: fdbfvuie
"""

from itertools import combinations

b = 0
while 1:
    a = [int(i) for i in input().split()]
    if a[0] == 0:
        break
    if b == 0:
        b = 1
    else:
        print()
    a.pop(0)
    comb = combinations(a, 6)
    for i in list(comb):
        print(" ".join([str(j) for j in i]))