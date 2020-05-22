#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 10:59 2020

@author: fdbfvuie
"""

import math

while True:
    n = int(input())
    if n == 0:
        break
    a = map(int, input().split())
    b = 1
    for i in a:
        b = int(abs(b * i) / math.gcd(b, i))
    print(b)