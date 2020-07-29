#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:26 2020

@author: fdbfvuie
"""

while 1:
    n = int(input())
    if n == 0:
        break
    a = []
    for i in range(n):
        b = 0
        c, d = map(int, input().split())
        if c > d:
            b = 2
        elif c == d:
            b = 1
        a.append([c + d, b])
    a.sort(reverse=True)
    for i in a:
        if i[1] == 2:
            print(">", end="")
        elif i[1] == 1:
            print("=", end="")
        else:
            print("<", end="")
        print(i[0], end=" ")
    print()