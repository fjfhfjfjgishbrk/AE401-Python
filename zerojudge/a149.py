#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 10:11 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    num = input()
    s = 1
    for j in num:
        s *= int(j)
    print(s)