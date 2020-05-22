#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 10:28 2020

@author: fdbfvuie
"""

while 1:
    try:
        n = int(input())
        prime = True
        for i in range(2, int(n/2) + 1):
            count = 0
            while n % i == 0:
                prime = False
                n = int(n / i)
                count += 1
            if count != 0:
                if count == 1:
                    print(i, end="")
                else:
                    print("{}^{}".format(i, count), end="")
                if n != 1:
                    print(" * ", end="")
        if prime:
            print(n, end="")
        print()
    except:
        break