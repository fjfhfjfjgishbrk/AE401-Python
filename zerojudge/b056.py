#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 12:00 2020

@author: fdbfvuie
"""

while 1:
    try:
        n = int(input())
        b = 0
        for i in range(n):
            a = [int(i) for i in input().split()]
            for j in range(n):
                R = a[j * 3]
                G = a[j * 3 + 1]
                B = a[j * 3 + 2]
                X = round(0.5149 * R + 0.3244 * G + 0.1607 * B, 4)
                Y = round(0.2654 * R + 0.6704 * G + 0.0642 * B, 4)
                Z = round(0.0248 * R + 0.1248 * G + 0.8504 * B, 4)
                print("{:.4f} {:.4f} {:.4f}".format(X, Y, Z))
                b += Y
        print("The average of Y is {}".format(round(b / (n ** 2), 4)))
        input()
    except:
        break