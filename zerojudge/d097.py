#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:54 2020

@author: fdbfvuie
"""

while 1:
    try:
        a = input().split()
        a.pop(0)
        b = []
        d = 0
        for i in range(1, len(a)):
            b.append(i)
        for i in range(len(a) - 1):
            if abs(int(a[i]) - int(a[i + 1])) in b:
                b.remove(abs(int(a[i]) - int(a[i + 1])))
            else:
                d = 1
                break
        if d == 1:
            print("Not jolly")
        else:
            print("Jolly")
    except:
        break