#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 11:39 2020

@author: fdbfvuie
"""

while 1:
    try:
        n, w = map(int, input().split())
        food = {}
        for i in range(n):
            a, b = map(str, input().split())
            food[a] = int(b)
        n = int(input())
        cal = 0
        for i in range(n):
            a, b = map(str, input().split())
            cal += food[a] * int(b)
        if cal >= (40 * w):
            print("Euan eats too much.")
        else:
            print("Euan you are doing a great job!")
    except:
        break