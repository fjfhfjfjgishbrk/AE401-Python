#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:27 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    input()
    a = [int(i) for i in input().split()]
    high = low = 0
    for j in range(0, len(a) - 1):
        if a[j] < a[j + 1]:
            high += 1
        elif a[j] > a[j + 1]:
            low += 1
    print("Case {}: {} {}".format(str(i + 1), str(high), str(low)))