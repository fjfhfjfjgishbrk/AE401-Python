#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:21 2020

@author: fdbfvuie
"""

input()
a = [int(i) for i in input().split()]
amin = min(a)
b = []
for i in range(len(a) - 1):
    if amin == a[i]:
        amin = min(a[i+1:])
    b.append(a[i] - amin)
print(max(b))