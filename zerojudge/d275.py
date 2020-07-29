#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:16 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    a = input()
    if a.count("M") == a.count("F") and a.count("M") > 1:
        print("LOOP")
    else:
        print("NO LOOP")