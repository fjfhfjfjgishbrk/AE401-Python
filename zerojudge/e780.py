#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 10:42 2020

@author: fdbfvuie
"""

n = int(input())
pos = 0
c = 0
for i in range(n):
    a = input()
    if a == "L":
        pos -= 1
    elif a == "R":
        pos += 1
    else:
        b = int(a.split()[1])
        if pos == b:
            c += 1
print(c)