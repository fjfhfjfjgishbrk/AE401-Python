#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 7 11:42 2020

@author: fdbfvuie
"""

input()
b = []
c = {"S": 1, "H": 2, "D": 3, "C": 4}
a = input().split()
for i in range(0, len(a), 2):
    b.append([a[i], a[i + 1]])
b.sort(key=lambda x: (-int(x[1]), c[x[0]]))
n = int(input())
print(b[n - 1][0], b[n - 1][1])