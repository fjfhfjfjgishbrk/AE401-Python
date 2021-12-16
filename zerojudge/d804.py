#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 10:46 2020

@author: fdbfvuie
"""

n, m = map(int, input().split())
a = [int(i) for i in input().split()]
a.sort(reverse=True)
b = 0
c = 0
for i in range(len(a)):
    b += a[i]
    if b >= m:
        print(i+1)
        c = 1
        break
if c == 0:
    print("OAQ")