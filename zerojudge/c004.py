#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 10:11 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if (a - b) % 2 != 0 or b > a:
        print("impossible")
    else:
        print((a - b) // 2 + b, (a - b) // 2)