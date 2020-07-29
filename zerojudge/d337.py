#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:11 2020

@author: fdbfvuie
"""

while 1:
    try:
        a = input()
        for ch in a:
            if '\u4e00' <= ch <= '\u9fff':
                print(ch, end="")
        print()
    except:
        break