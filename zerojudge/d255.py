#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 10:33 2020

@author: fdbfvuie
"""

import math
while 1:
    n = int(input())
    if n == 0:
        break
    g = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            g += math.gcd(i, j)
    print(g)