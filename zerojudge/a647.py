#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 9 20:24 2020

@author: fdbfvuie
"""

while True:
    try:
        n = int(input())
        for i in range(n):
            a = input().split(" ")
            percent = (int(a[1]) - int(a[0])) / int(a[0]) * 100

            if percent >= 0:
                print(str('{:.2f}'.format(round(percent + 0.000001, 2))) + "% ", end="")
            else:

                print(str('{:.2f}'.format(round(percent - 0.000001, 2))) + "% ", end="")
            if percent >= 10 or percent <= -7:
                print("dispose")
            else:
                print("keep")

    except:
        break