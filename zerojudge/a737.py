#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 7 11:31 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    a = [int(i) for i in input().split()]
    a.pop(0)
    a.sort()
    total = 0
    b = a[(len(a) - 1) // 2]
    for j in a:
        total += abs(j - b)
    print(total)