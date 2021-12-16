#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 11:10 2020

@author: fdbfvuie
"""

import math
n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    if b >= a:
        print(1)
    elif c >= b:
        print("Poor Snail")
    else:
        print(int(math.ceil((a - b) / (b - c)) + 1))