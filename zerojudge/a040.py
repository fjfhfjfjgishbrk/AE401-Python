#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 6 11:01 2020

@author: fdbfvuie
"""

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834]
while True:
    try:
        n = [int(i) for i in input().split(" ")]
        haveNum = False
        for i in a:
            if i >= n[0] and i <= n[1]:
                print(i, end=" ")
                haveNum = True
        if not haveNum:
            print("none")
        else:
            print()
    except:
        break