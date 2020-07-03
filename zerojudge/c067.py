#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:53 2020

@author: fdbfvuie
"""

c = 0
while 1:
    c += 1
    n = int(input())
    if n == 0:
        break
    a = [int(i) for i in input().split()]
    avg = int(sum(a) / n)
    b = 0
    for i in a:
        if i > avg:
            b += (i - avg)
    print("Set #{}".format(str(c)))
    print("The minimum number of moves is {}.".format(str(b)))
    print()