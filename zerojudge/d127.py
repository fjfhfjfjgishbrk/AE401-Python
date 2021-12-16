#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 10:50 2020

@author: fdbfvuie
"""

while 1:
    try:
        a = int(input())
        l = a // 4
        w = a / 2 - l
        print(int(l*w))
    except:
        break