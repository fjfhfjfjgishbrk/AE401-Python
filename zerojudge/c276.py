#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 09 20:38 2020

@author: fdbfvuie
"""

num = input()
while True:
    try:
        n = input()
        for i in range(int(n)):
            guessNum = input()
            a = b = 0
            for j in range(len(num)):
                for k in range(len(guessNum)):
                    if num[j] == guessNum[k]:
                        if j == k:
                            a += 1
                        else:
                            b += 1
            print(str(a) + "A" + str(b) + "B")

    except:
        break