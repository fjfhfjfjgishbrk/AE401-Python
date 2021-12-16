#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:31 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    a = int(input())
    print("Case {}: ".format(i + 1), end="")
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        print("a leap year")
    else:
        print("a normal year")