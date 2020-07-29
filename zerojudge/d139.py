#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 11:39 2020

@author: fdbfvuie
"""

while 1:
    try:
        a = input()
        b = ""
        c = 0
        for i in a:
            if i != b:
                if c > 2:
                    print(str(c) + b, end="")
                elif c == 2:
                    print(b*2, end="")
                else:
                    print(b, end="")
                b = i
                c = 1
            else:
                c += 1
        if c > 2:
            print(str(c) + b)
        elif c == 2:
            print(b * 2)
        else:
            print(b)
    except:
        break