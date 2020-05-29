#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 10:50 2020

@author: fdbfvuie
"""

b = ["kuti", 'shata', 'hajar', 'lakh']
c = 0
while 1:
    try:
        num = input()
        c += 1
        print("{}.".format(c), end=" ")
        if int(num) == 0:
            print("0", end="")
        a = []
        append = True
        for i in range(1, len(num) + 1):
            if append:
                a.append(int(num[-i]))
                append = False
            else:
                a[-1] = a[-1] + int(num[-i]) * 10
                append = True
            if len(a) % 4 == 2:
                append = True
        for i in range(len(a)-1, -1, -1):
            if i == 0:
                if a[i] != 0:
                    print(a[i], end=" ")
            elif a[i] == 0 and i % 4 == 0:
                print(b[i % 4], end=" ")
            elif a[i] != 0:
                print(a[i], b[i % 4], end=" ")
        print()
    except:
        break