#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 6 10:55 2020

@author: fdbfvuie
"""

import sys
n = int(input())
for i in range(n):
    a = int(input())
    b = []
    for j in range(a):
        b.append(int(sys.stdin.readline().strip()))
    b.sort()
    print(b[(len(b) - 1) // 2])