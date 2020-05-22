#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 10:26 2020

@author: fdbfvuie
"""

while 1:
    try:
        a = input().split(" ")
        if a[0] == a[1]:
            print(a[1])
        else:
            print(str(int(a[1]) + 1))
    except:
        break