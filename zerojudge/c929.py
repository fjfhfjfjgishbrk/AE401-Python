#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:12 2020

@author: fdbfvuie
"""

while 1:
    try:
        a = input()
        b = input().split(a)
        for i in b:
            print(i)
    except:
        break