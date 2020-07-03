#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:22 2020

@author: fdbfvuie
"""

import math
a = [1, 1]
for i in range(2, 93):
    a.append(a[i-2] + a[i-1])
while 1:
    try:
        b, c = map(int, input().split())
        print(a[math.gcd(b, c) - 1])
    except:
        break