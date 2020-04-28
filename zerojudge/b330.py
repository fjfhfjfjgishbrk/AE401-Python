#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 10:36 2020

@author: fdbfvuie
"""

a = input().split()
n = a[0]
x = a[1]
count = 0

for i in range(int(n)):
    for j in str(i + 1):
        if j == x:
            count += 1
print(count)