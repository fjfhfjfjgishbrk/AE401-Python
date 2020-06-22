#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 4 10:18 2020

@author: fdbfvuie
"""

a = input().split()
b = input().split()
c = [int(i) for i in input().split()]
d = 0
e = True
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            if i == 2:
                d = max(0, d - c[j])
                e = False
            else:
                d += c[j]
if e:
    d *= 2
print(d)