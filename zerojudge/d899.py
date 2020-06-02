#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 10:53 2020

@author: fdbfvuie
"""

a, b = map(int, input().split())
c = 0
for i in range(a, b+1):
    for j in str(i):
        if j == "2":
            c += 1
print(c)