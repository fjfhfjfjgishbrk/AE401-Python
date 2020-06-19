#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 10:50 2020

@author: fdbfvuie
"""

n = int(input())
input()
for i in range(n):
    a = int(input())
    b = int(input())
    for j in range(b):
        for k in range(1, a+1):
            print(str(k)*k)
        for k in range(a-1, 0, -1):
            print(str(k)*k)
        print()