#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 11:04 2020

@author: fdbfvuie
"""

while 1:
    try:
        a = [int(i) for i in input().split()]
        b = 0
        for i in range(len(a)):
            c = a[i]
            if b == 0:
                if c == 0:
                    continue
                else:
                    b = 1
                    if c < 0:
                        print("-", end="")
                    if abs(c) != 1 or i == 8:
                        print(abs(c), end="")
                    if i <= 6:
                        print("x^{}".format(8-i), end="")
                    elif i == 7:
                        print("x", end="")
            else:
                if c == 0:
                    continue
                else:
                    if c < 0:
                        print(" - ", end="")
                    else:
                        print(" + ", end="")
                    if abs(c) != 1 or i == 8:
                        print(abs(c), end="")
                    if i <= 6:
                        print("x^{}".format(8 - i), end="")
                    elif i == 7:
                        print("x", end="")
        if b == 0:
            print(0, end="")
        print()
    except:
        break