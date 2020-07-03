#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 1 11:35 2020

@author: fdbfvuie
"""

n = int(input().split()[0])
for i in range(n):
    a = input().split()
    b = input().split()
    c = len(set(a).intersection(b))
    print(c)