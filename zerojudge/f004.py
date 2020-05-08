#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 8 10:47 2020

@author: fdbfvuie
"""

a = [1, 5, 10, 50, 100, 500, 1000]
def b(t1, t2):
    return str("{}*{}".format(t1, t2))

while True:
    try:
        amount = [0, 0, 0, 0, 0, 0, 0]
        n = int(input())
        startN = n
        for i in range(1, len(a) + 1):
            while n >= a[-i]:
                amount[-i] += 1
                n -= a[-i]
        print(startN, end=" = ")
        printText = []
        for i in range(1, len(a) + 1):
            if amount[-i] != 0:
                printText.append(b(a[-i], amount[-i]))
        print(" + ".join(printText))
    except:
        break