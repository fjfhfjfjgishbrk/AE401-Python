#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:13 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    m = int(input())
    d = 0
    for j in range(m):
        a, b, c = map(int, input().split())
        d += a * c
    print(d)