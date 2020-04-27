#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 20:35 2020

@author: fdbfvuie
"""

while True:
    try:
        n = input()
        a = input()
        a = a.split(" ")
        a = [int(i) for i in a]
        a.sort()

        for i in range(int(n)):
            print(a[i], end=" ")
        print()

    except:
        break