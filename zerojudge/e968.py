#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 10:18 2020

@author: fdbfvuie
"""

n = int(input())
a = [int(i) for i in input().split(" ")]
for i in range(n, 0, -1):
    if i in a:
        continue
    print("No.", i)