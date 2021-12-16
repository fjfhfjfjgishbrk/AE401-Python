#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 1 11:58 2020

@author: fdbfvuie
"""

a = input()
b = ""
temp = a[0]
for i in range(1, len(a)):
    if ord(temp[-1]) + 1 == ord(a[i]):
        temp += a[i]
    else:
        if len(temp) >= len(b):
            b = temp
        temp = a[i]
if len(temp) >= len(b):
    b = temp
print(len(b), b)