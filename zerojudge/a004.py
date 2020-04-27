#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 06 19:52 2020

@author: fdbfvuie
"""

while 1:
    try:
        year = int(input())
    except:
        break

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print("閏年")
    else:
            print("平年")