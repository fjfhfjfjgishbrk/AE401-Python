#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:41 2020

@author: fdbfvuie
"""

while 1:
    a, b = map(int, input().split())
    if a == -1:
        break
    print(min(abs(a - b), min(a + 100, b + 100) - max(a, b)))