#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 20:39 2020

@author: fdbfvuie
"""

while True:
    try:
        n = int(input())
        numArray = input().split(" ")
        outArray = [[], [], [], [], [], [], [], [], [], []]
        for i in numArray:
            outArray[int(i[-1])].append(int(i))
        for i in outArray:
            i.sort(reverse=True)
            for j in i:
                print(j, end=" ")
        print()
    except:
        break