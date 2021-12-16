#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:29 2020

@author: fdbfvuie
"""

while 1:
    try:
        a = set(input().split())
        b = set(input().split())
        if a == b:
            print("A equals B")
        elif a.issubset(b):
            print("A is a proper subset of B")
        elif b.issubset(a):
            print("B is a proper subset of A")
        elif a.isdisjoint(b):
            print("A and B are disjoint")
        else:
            print("I'm confused!")
    except:
        break