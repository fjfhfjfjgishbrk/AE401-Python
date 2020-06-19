#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 12:00 2020

@author: fdbfvuie
"""

import sys
a = {"0 1 0 1": "A", "0 1 1 1": "B", "0 0 1 0": "C", "1 1 0 1": "D", "1 0 0 0": "E", "1 1 0 0": "F"}
while 1:
    try:
        n = int(input())
        for i in range(n):
            print(a[sys.stdin.readline().strip()], end="")
        print()
    except:
        break