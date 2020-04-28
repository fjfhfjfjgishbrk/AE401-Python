#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:45 2020

@author: fdbfvuie
"""

while True:
    try:
        n = [int(i) for i in input().split(" ")]
        print(n[0], n[1], n[2], end=". ")

        if n[0] * n[2] >= n[1]:
            print("I will make it!")
        else:
            print("I will be late!")

    except:
        break