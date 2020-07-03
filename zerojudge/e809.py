#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:43 2020

@author: fdbfvuie
"""

a = input()
b = input()
c = [0]
for i in a:
    c.append(b.count(i) + c[-1])
n = int(input())
for i in range(n):
    d = int(input())
    for j in range(len(c)):
        if d <= c[j]:
            print(a[j-1])
            break