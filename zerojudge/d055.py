#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:13 2020

@author: fdbfvuie
"""

n = int(input())
for i in range(n):
    Ax, Ay, Bx, By, Cx, Cy = map(float, input().split())
    print(round(abs(Ax*By - Ay*Bx + Bx*Cy - By*Cx + Cx*Ay - Cy*Ax) / 14))