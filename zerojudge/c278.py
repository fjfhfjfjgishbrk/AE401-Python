#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 3 11:12 2020

@author: fdbfvuie
"""

n = int(input())
a = []
while len(a) < n:
    a += [int(i) for i in input().strip().split()]
a.sort()
b = 0
for i in range(0, len(a), 2):
    b += a[i + 1] - a[i]
print(b)