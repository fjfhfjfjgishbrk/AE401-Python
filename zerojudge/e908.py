#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 10:17 2020

@author: fdbfvuie
"""

a = {"Sunday" : 0, "Monday" : 1, "Tuesday" : 2, "Wednesday" : 3, "Thursday" : 4, "Friday" : 5, "Saturday" : 6}
n = a[input()]
ans = (n+int(input())) % 7
for i, j in a.items():
    if j == ans:
        print(i)
        break