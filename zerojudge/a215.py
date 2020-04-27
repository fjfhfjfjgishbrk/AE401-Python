#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 12:03 2020

@author: fdbfvuie
"""

while True:
    try:
        a, b = map(int, input().split(" "))
        sum = 0
        count = 1

        while True:
            sum += a
            if sum > b:
                break
            a += 1
            count += 1

        print(count)

    except:
        break