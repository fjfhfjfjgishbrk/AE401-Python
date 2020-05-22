#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 10:58 2020

@author: fdbfvuie
"""

n = int(input())
b = [0, 0, 0]
c = 0
for i in range(n):
    a = input().strip()
    if a == "Get_Kill":
        c += 1
        b[0] += 1
        if c >= 8:
            print("LEGENDARY!")
        elif c == 7:
            print("GUALIKE!")
        elif c == 6:
            print("DOMINATING!")
        elif c == 5:
            print("UNSTOPPABLE!")
        elif c == 4:
            print("RAMPAGE~")
        elif c == 3:
            print("KILLING SPREE!")
        else:
            print("You have slain an enemie.")
    elif a == "Get_Assist":
        b[2] += 1
    elif a == "Die":
        b[1] += 1
        if c >= 3:
            print("SHUTDOWN.")
        else:
            print("You have been slained.")
        c = 0
print("{}/{}/{}".format(b[0], b[1], b[2]))