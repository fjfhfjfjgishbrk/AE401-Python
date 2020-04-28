#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 10:09 2020

@author: fdbfvuie
"""

while True:
    try:
        n = input()

        for i in range(int(n)):
            if i == 0 or i % 7 == 0:
                continue
            else:
                print(i, end=" ")
        print()

    except:
        break