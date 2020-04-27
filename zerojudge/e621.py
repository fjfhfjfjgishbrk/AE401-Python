#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 10:30 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    a = [int(j) for j in input().split(" ")]
    noPark = True
    
    for j in range(a[0] + 1, a[1], 1):
        if j % a[2] != 0:
            print(j, end=" ")
            noPark = False

    if noPark:
        print("No free parking spaces.", end = "")
    print()