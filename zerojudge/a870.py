#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 10:46 2020

@author: fdbfvuie
"""

b = []
while 1:
    a = input().split()
    if a[0] == "SHOW":
        break
    elif a[0] == "ADD":
        b.append(a[1])
    elif a[0] == "INSERT":
        b.insert(b.index(a[2]), a[1])
    elif a[0] == "REMOVE":
        b.remove(a[1])
print(" ".join(b))