#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 3 11:42 2020

@author: fdbfvuie
"""

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a, b, c = map(int, input().split())
s = 0
for i in range(1, c+1):
    if i % a == 0 or i % b == 0:
        s += i
print(alpha[(s-1) % 26])