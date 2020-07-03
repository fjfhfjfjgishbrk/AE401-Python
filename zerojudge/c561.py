#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 10:37 2020

@author: fdbfvuie
"""

input()
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i][::-1])
a.sort()
print(a[-1])