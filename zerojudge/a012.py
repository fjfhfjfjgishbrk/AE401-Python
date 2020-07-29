#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:25 2020

@author: fdbfvuie
"""

while 1:
    try:
        a, b = map(int, input().split())
        print(abs(a-b))
    except:
        break