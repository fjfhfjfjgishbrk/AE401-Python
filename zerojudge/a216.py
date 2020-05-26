#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 10:46 2020

@author: fdbfvuie
"""

while True:
    try:
        n = int(input())
        a = n * (n + 1) / 2
        b = n * (n + 1) * (n + 2) / 6
        print(str(int(a)) + " " + str(int(b)))
    except:
        break