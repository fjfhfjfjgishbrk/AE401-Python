#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:16 2020

@author: fdbfvuie
"""

a = input().split()
b = list(dict.fromkeys(a))
for i in b:
    if a.count(i) % 3 != 0:
        print(i)
        break