#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 10:30 2020

@author: fdbfvuie
"""

import math
_1_50 = 1 << 50
def isqrt(x):
    if x < _1_50:
        return int(math.sqrt(x))
    n = int(x)
    if n <= 1:
        return n
    r = 1 << ((n.bit_length() + 1) >> 1)
    while True:
        newr = (r + n // r) >> 1
        if newr >= r:
            return r
        r = newr
n = int(input())
for i in range(n):
    input()
    print(isqrt(int(input())))