#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 3 11:03 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    a = int(input())
    b = int(input())
    a = a if a % 2 else a + 1
    b = b if b % 2 else b - 1
    sum = (a + b) * ((b - a) / 2 + 1) / 2
    print("Case {}: {}".format(str(i+1), str(int(sum))))