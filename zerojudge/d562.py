#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 09:42 2020

@author: fdbfvuie
"""

while True:
    try:
        n = int(input())
        a = [int(i) for i in input().split()]
        for i in range(n):
            print(" ".join([str(j) for j in a]))
            a.pop(0)
            a.reverse()
        print()
    except:
        break