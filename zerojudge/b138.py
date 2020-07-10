#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 7 10:55 2020

@author: fdbfvuie
"""

a = [int(i) for i in input().split()]
b = int(input())
print(sum(i <= (b + 30) for i in a))