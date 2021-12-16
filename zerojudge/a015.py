#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 6 10:43 2020

@author: fdbfvuie
"""

while True:
    try:
        n = [int(i) for i in input().split(" ")]
        res = []
        for i in range(n[0]):
            res.append(input().split(" "))
        for i in range(n[1]):
            for j in range(n[0]):
                print(res[j][i], end=" ")
            print()
        print()
    except:
        break