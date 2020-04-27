#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 10:34 2020

@author: fdbfvuie
"""

mod3 = [0, 0, 0]
while True:
    try:
        a = int(input())
        for i in range(a):
            n = int(input())
            mod3[n % 3] += 1

    except:
        print(mod3[0], mod3[1], mod3[2])
        break