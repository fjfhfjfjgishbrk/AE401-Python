#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:27 2020

@author: fdbfvuie
"""

while True:
    try:
        a = input().split(" ")
        n = input().split(" ")
        s = [0]

        for i in range(len(n)):
            s.append(int(s[i]) + int(n[i]))

        for i in range(int(a[1])):
            c = input().split(" ")
            print(s[int(c[1])] - s[int(c[0]) - 1])

    except:
        break