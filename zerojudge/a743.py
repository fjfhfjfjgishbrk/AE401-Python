#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 11:21 2020

@author: fdbfvuie
"""

a = {}
n = int(input())
for i in range(n):
    b = input().split()
    if b[0] in a:
        a[b[0]] += 1
    else:
        a[b[0]] = 1
b = sorted(a.items(), key=lambda x: x[0])
for i in b:
    print(i[0], i[1])