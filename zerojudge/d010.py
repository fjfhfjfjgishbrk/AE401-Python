#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 3 11:16 2020

@author: fdbfvuie
"""

while 1:
    try:
        a = int(input())
        facSum = 1
        for j in range(2, int(a**0.5)+1):
            if (a % j == 0):
                if(a / j == j):
                    facSum += j
                else:
                    facSum += j + int(a/j)
        if facSum > a:
            print("盈數")
        elif facSum < a:
            print("虧數")
        else:
            print("完全數")
    except:
        break