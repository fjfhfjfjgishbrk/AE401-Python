#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:18 2020

@author: fdbfvuie
"""

while 1:
    a = int(input())
    if a == 0:
        break
    print(int(a % 17 == 0))