#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:19 2020

@author: fdbfvuie
"""

input()
a = [int(i) for i in input().split()]
b = [str(a[0])]
for i in range(1, len(a)):
    b.append(str(a[i] - a[i-1]))
print(" ".join(b))