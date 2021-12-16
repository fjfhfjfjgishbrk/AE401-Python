#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:57 2020

@author: fdbfvuie
"""

import sys
n = int(input())
for i in range(n):
    a = int(sys.stdin.readline().strip(), 2)
    if a % 3 == 0:
        print("Yes")
    else:
        print("No")