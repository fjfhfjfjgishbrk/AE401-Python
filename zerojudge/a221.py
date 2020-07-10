#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 7 10:21 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    a = input()
    b = input()
    print("Case {}: ".format(str(i+1)), end="")
    if a == b:
        print("Yes")
    else:
        if a.replace(" ","") == b:
            print("Output Format Error")
        else:
            print("Wrong Answer")