#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 4 10:28 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    a = int(input())
    b = [0] * 10
    for j in range(1, a + 1):
        for k in str(j):
            b[int(k)] += 1
    print(" ".join([str(j) for j in b]))