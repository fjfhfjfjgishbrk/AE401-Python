#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 09:42 2020

@author: fdbfvuie
"""

def f(x):
    if x == 1:
        return 1
    elif x%2 == 0:
        return f(int(x / 2))
    else:
        return f(x - 1) + f(x + 1)

print(f(int(input())))