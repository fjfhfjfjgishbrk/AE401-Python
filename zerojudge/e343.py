#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 09:42 2020

@author: fdbfvuie
"""

while 1:
    try:
        a = int(input())
        b = int(input()) / 100
        print(round(a/(b*b),1))
    except:
        break