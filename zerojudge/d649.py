#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:44 2020

@author: fdbfvuie
"""

while 1:
    try:
        n = int(input())
        for i in range(n):
            print("_"*(n-i-1), end="")
            print("+"*(i+1))
        print()
    except:
        break