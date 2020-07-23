#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 10:55 2020

@author: fdbfvuie
"""

input()
a = [int(i) for i in input().split()]
b = 0
for i in a:
    if i <= 10:
        b += 1
print(b)