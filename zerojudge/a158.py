#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:30 2020

@author: fdbfvuie
"""

import math
n = int(input())
for i in range(n):
    a = [int(i) for i in input().split()]
    b = 0
    for j in range(len(a)):
        for k in range(j+1, len(a)):
            b = max(b, math.gcd(a[j], a[k]))
    print(b)