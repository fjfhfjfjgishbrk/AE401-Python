#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 11:51 2020

@author: fdbfvuie
"""

while 1:
    try:
        n, m = map(int, input().split())
        a = []
        for i in range(n):
            a.append(input().split())
        for i in range(m):
            b = input().split()
            if b[0] == "brand":
                for j in a:
                    if j[0] == b[1]:
                        print(" ".join(j))
            else:
                for j in a:
                    if j[1] == b[1]:
                        print(" ".join(j))
        input()

    except:
        break