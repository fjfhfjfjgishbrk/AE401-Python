#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 10:41 2020

@author: fdbfvuie
"""

import sys
while 1:
    n = int(input())
    if n == 0:
        break
    a = sys.stdin.readline().strip().split()
    b = [0] * 101
    c = 0
    for i in a:
        if int(i) % 100 == 0:
            c += b[100]
        else:
            c += b[int(i) % 100]
        b[100 - (int(i) % 100)] += 1
    print(c)