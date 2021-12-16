#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 6 10:50 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    c = []
    for j in range(a):
        c += input().strip().split()
    d = c.copy()
    d.reverse()
    if d == c:
        print("go forward")
    else:
        print("keep defending")