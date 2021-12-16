#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 3 12:10 2020

@author: fdbfvuie
"""

while 1:
    try:
        a, b = map(int, input().split())
        if b == 0:
            if a == 0:
                print("Ok!")
            else:
                print("Impossib1e!")
        else:
            if a % b == 0:
                print("Ok!")
            else:
                print("Impossib1e!")
    except:
        break