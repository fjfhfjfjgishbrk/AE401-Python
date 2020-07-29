#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:56 2020

@author: fdbfvuie
"""

while 1:
    try:
        a = float(input())
        print("|{0:.4f}|=".format(a), end="")
        print("{0:.4f}".format(abs(a)))
    except:
        break