#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 11:48 2020

@author: fdbfvuie
"""

while 1:
    try:
        n = int(input())
        a = 5
        c = 0
        while a <= n:
            c += n // a
            a *= 5
        print(c)
    except:
        break