#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 12:08 2020

@author: fdbfvuie
"""

b = [1]
c2 = 0
while True:
    c2 += 1
    for i in range(c2 + 1):
        for j in range(c2 + 1):
            for k in range(c2 + 1):
                if i + j + k == c2:
                    d = 2 ** i * 3 ** j * 5 ** k
                    if d not in b:
                        b.append(d)
    b.sort()
    if len(b) >= 1500:
        if b[1499] < 2 ** c2:
            break
print("The 1500'th ugly number is {}.".format(b[1499]))