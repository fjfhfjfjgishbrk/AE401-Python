#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 1 10:09 2020

@author: fdbfvuie
"""

while 1:
    try:
        n = int(input())
        if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
            print("a leap year")
        else:
            print("a normal year")
    except:
        break