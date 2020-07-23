#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:14 2020

@author: fdbfvuie
"""

import math
while 1:
    try:
        m, k = map(int, input().split())
        a = [int(i) for i in input().split()]
        b = 1
        for i in a:
            b = int(i * b / math.gcd(i, b))
        c = 1
        while True:
            print(b * c + k, end=" ")
            c += 1
            if b*c + k > m:
                break
        print()
    except:
        break