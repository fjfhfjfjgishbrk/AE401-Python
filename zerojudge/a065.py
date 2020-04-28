#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 10:24 2020

@author: fdbfvuie
"""

while True:
    try:
        n = input()
        for i in range(len(n) - 1):
            print(abs(ord(n[i]) - ord(n[i+1])), end="")
        print()

    except:
        break