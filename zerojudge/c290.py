#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:25 2020

@author: fdbfvuie
"""

a = input()
b = 0
for i in range(len(a)):
    b += int(a[i]) if i % 2 else -int(a[i])
print(abs(b))