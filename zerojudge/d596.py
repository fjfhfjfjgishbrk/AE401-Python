#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:37 2020

@author: fdbfvuie
"""

def aa(num, p):
    if num == 1:
        bomb[1] = p
        bomb[3] = p
    elif num == 2:
        bomb[0] = p
        bomb[2] = p
        bomb[4] = p
    elif num == 3:
        bomb[1] = p
        bomb[5] = p
    elif num == 4:
        bomb[0] = p
        bomb[4] = p
        bomb[6] = p
    elif num == 5:
        bomb[1] = p
        bomb[3] = p
        bomb[5] = p
        bomb[7] = p
    elif num == 6:
        bomb[2] = p
        bomb[4] = p
        bomb[8] = p
    elif num == 7:
        bomb[3] = p
        bomb[7] = p
    elif num == 8:
        bomb[6] = p
        bomb[4] = p
        bomb[8] = p
    else:
        bomb[7] = p
        bomb[5] = p


n = int(input())
for i in range(n):
    bomb = [0] * 9
    a, b, c = map(int, input().split())
    aa(a, 1)
    aa(b, 0)
    aa(c, 0)
    a = True
    for j in range(9):
        if bomb[j]:
            print(j+1, end=" ")
            a = False
    if a:
        print("Empty")
    else:
        print()