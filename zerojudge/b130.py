#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 11:16 2020

@author: fdbfvuie
"""

while 1:
    try:
        input()
        a = [int(i) for i in input().split()]
        a = list(dict.fromkeys(a))
        a.sort()
        print(len(a))
        print(" ".join([str(i) for i in a]))
    except:
        break