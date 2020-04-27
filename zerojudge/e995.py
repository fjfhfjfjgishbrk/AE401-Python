#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:51 2020

@author: fdbfvuie
"""

import math

v = 0
n = 1
numList = [0]

while True:
    if v > 9000000000:
        break
    v += 9 * (10 ** (n-1)) * n
    numList.append(numList[n - 1] + 9 * (10 ** (n-1)) * n)
    n += 1

while True:
    try:
        inp = int(input())
        a = 0

        for i in range(len(numList)):
            if numList[i] >= inp:
                a = i
                break

        numIn = math.ceil((inp - numList[a - 1]) / a)
        numLeft = (inp - numList[a - 1] - 1) % a
        print(str(10 ** (a - 1) + numIn - 1)[numLeft])

    except:
        break