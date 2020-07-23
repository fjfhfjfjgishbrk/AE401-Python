#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:04 2020

@author: fdbfvuie
"""

while 1:
    try:
        n = int(input())
        print(3 * (2 * int((n + 1) / 2) ** 2 - 3))
    except:
        break