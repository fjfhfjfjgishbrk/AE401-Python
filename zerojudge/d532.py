#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:33 2020

@author: fdbfvuie
"""

i, b = map(int, input().split())
c = 0
for a in range(i, b+1):
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        c += 1
print(c)