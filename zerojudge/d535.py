#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 9 09:39 2020

@author: fdbfvuie
"""

a = input()
b = False
c = "2468"
if a == a[::-1] and a.isnumeric():
    for i in range(len(a) - 1):
        if int(a[i+1]) > int(a[i]) * 2:
            b = True
            break
else:
    b = True
if b:
    print("INCORRECT")
else:
    for i in a:
        if i in c:
            print(i, end="")
            b = True
    if not b:
        print("0")