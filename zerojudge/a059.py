#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 10:39 2020

@author: fdbfvuie
"""

import math

n = int(input())
for i in range(n):
    a = int(input())
    b = int(input())
    sum = 0

    for j in range(math.ceil(math.sqrt(a)), math.floor(math.sqrt(b)) + 1, 1):
        sum += j ** 2

    print("Case " + str(i+1) + ": " + str(sum))