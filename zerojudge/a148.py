#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 10:40 2020

@author: fdbfvuie
"""

while True:
    try:
        a = [int(i) for i in input().split(" ")]
        sum = 0
        for i in range(1, len(a)):
            sum += a[i]
        b = "no" if sum / a[0] > 59 else "yes"
        print(b)
    except:
        break