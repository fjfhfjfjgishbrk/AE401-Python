#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 9 10:25 2020

@author: fdbfvuie
"""

while True:
    try:
        n = int(input())
        amount = input().split(" ")
        total = 0

        for i in range(n):
            total += (i+1) * int(amount[i])
        print(total)

    except:
        break