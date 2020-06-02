#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:01 2020

@author: fdbfvuie
"""

while 1:
    a = int(input())
    if a == 0:
        break
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        print("a leap year")
    else:
        print("a normal year")