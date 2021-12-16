#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:28 2020

@author: fdbfvuie
"""

b = 0
while 1:
    try:
        a = input()
        c = a
        d = 0
        for i in range(len(a)):
            if a[i] == "\"":
                if b % 2 == 0:
                    c = c[:i+d] + "``" + c[i+d+1:]
                else:
                    c = c[:i+d] + "''" + c[i+d+1:]
                b += 1
                d += 1
        print(c)
    except:
        break