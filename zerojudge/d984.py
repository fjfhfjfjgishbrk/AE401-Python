#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:15 2020

@author: fdbfvuie
"""

while 1:
    try:
        a, b, c = map(int, input().split())
        if a > b and a > c:
            if b + c > a:
                if b > c:
                    print("B")
                else:
                    print("C")
            else:
                print("A")
        if b > a and b > c:
            if a + c > b:
                if a > c:
                    print("A")
                else:
                    print("C")
            else:
                print("B")
        if c > b and c > a:
            if a + b > c:
                if b > a:
                    print("B")
                else:
                    print("A")
            else:
                print("C")
    except:
        break