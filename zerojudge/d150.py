#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:14 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    c = int(input())
    a = [int(i) for i in input().split()]
    b = 0
    a.sort(reverse=True)
    for j in range(2, c, 3):
        b += a[j]
    print(b)