#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 1 10:34 2020

@author: fdbfvuie
"""

a, b, c = map(int, input().split(" "))
for i in range(a, b, c):
    print(i, end=" ")
print(b)