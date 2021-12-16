#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 11:21 2020

@author: fdbfvuie
"""

input()
a = "".join(input().split()).strip("09")
b = 0
for i in range(1, len(a) - 1):
    if a[i] == "0" and a[i - 1] != "9" and a[i + 1] != "9":
        b += 1
print(b)