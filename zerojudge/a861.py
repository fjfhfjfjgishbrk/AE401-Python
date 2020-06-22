#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:40 2020

@author: fdbfvuie
"""

while 1:
    try:
        a, b = map(int, input().split())
        print((a+b)*2)
    except:
        break