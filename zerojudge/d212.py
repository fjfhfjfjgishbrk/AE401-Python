#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 11:31 2020

@author: fdbfvuie
"""

a = [0, 1, 2]
for i in range(3, 101):
    a.append(a[i-2] + a[i-1])
while 1:
    try:
        print(a[int(input())])
    except:
        break