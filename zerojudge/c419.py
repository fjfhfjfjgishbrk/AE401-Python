#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 09:45 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    print("_"*(n-i-1), end="")
    print("*"*(i+1))