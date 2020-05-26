#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:26 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    a = int(input())
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        print("a leap year")
    else:
        print("a normal year")