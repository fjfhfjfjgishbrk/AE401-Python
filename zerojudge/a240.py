#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 7 10:17 2020

@author: fdbfvuie
"""

a = "0588235294117647"
b = [0, 5, 13, 21, 23, 26, 31, 33, 42, 46, 47, 48, 55, 61, 65, 0]
n = int(input())
for i in range(n):
    c = int(input())
    print(a[(c-1) % 16], (c//16) * 72 + b[(c-1) % 16])