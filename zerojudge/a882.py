#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 3 11:54 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    a = input()
    b = 0
    for j in a:
        if j == "X":
            b += 2
        elif j == "H":
            b += 1
    print(b)