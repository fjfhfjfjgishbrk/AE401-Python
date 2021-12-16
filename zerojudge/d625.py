#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 6 11:29 2020

@author: fdbfvuie
"""

import sys
n = int(input())
a = []
for i in range(n):
    a.append(list(sys.stdin.readline().strip()))
for i in range(1, n-1):
    for j in range(1, n-1):
        if a[i][j] == "*":
            for k in range(3):
                a[i - 1][j - 1 + k] = 1 if a[i - 1][j - 1 + k] == "-" else a[i - 1][j - 1 + k] + 1 if a[i - 1][j - 1 + k] != "*" else "*"
                a[i + 1][j - 1 + k] = 1 if a[i + 1][j - 1 + k] == "-" else a[i + 1][j - 1 + k] + 1 if a[i + 1][j - 1 + k] != "*" else "*"
            a[i][j - 1] = 1 if a[i][j - 1] == "-" else a[i][j - 1] + 1 if a[i][j - 1] != "*" else "*"
            a[i][j + 1] = 1 if a[i][j + 1] == "-" else a[i][j + 1] + 1 if a[i][j + 1] != "*" else "*"
for j in range(1, n-1):
    if a[0][j] == "*":
        for k in range(3):
            a[1][j - 1 + k] = 1 if a[1][j - 1 + k] == "-" else a[1][j - 1 + k] + 1 if a[1][j - 1 + k] != "*" else "*"
        a[0][j - 1] = 1 if a[0][j - 1] == "-" else a[0][j - 1] + 1 if a[0][j - 1] != "*" else "*"
        a[0][j + 1] = 1 if a[0][j + 1] == "-" else a[0][j + 1] + 1 if a[0][j + 1] != "*" else "*"
for j in range(1, n-1):
    if a[n-1][j] == "*":
        for k in range(3):
            a[n-2][j - 1 + k] = 1 if a[n-2][j - 1 + k] == "-" else a[n-2][j - 1 + k] + 1 if a[n-2][j - 1 + k] != "*" else "*"
        a[n-1][j - 1] = 1 if a[n-1][j - 1] == "-" else a[n-1][j - 1] + 1 if a[n-1][j - 1] != "*" else "*"
        a[n-1][j + 1] = 1 if a[n-1][j + 1] == "-" else a[n-1][j + 1] + 1 if a[n-1][j + 1] != "*" else "*"
for i in range(1, n-1):
    if a[i][0] == "*":
        for k in range(2):
            a[i - 1][k] = 1 if a[i - 1][k] == "-" else a[i - 1][k] + 1 if a[i - 1][k] != "*" else "*"
            a[i + 1][k] = 1 if a[i + 1][k] == "-" else a[i + 1][k] + 1 if a[i + 1][k] != "*" else "*"
        a[i][1] = 1 if a[i][1] == "-" else a[i][1] + 1 if a[i][1] != "*" else "*"
for i in range(1, n-1):
    if a[i][n-1] == "*":
        for k in range(2):
            a[i - 1][n-1 - k] = 1 if a[i - 1][n-1 - k] == "-" else a[i - 1][n-1 - k] + 1 if a[i - 1][n-1 - k] != "*" else "*"
            a[i + 1][n-1 - k] = 1 if a[i + 1][n-1 - k] == "-" else a[i + 1][n-1 - k] + 1 if a[i + 1][n-1 - k] != "*" else "*"
        a[i][n-2] = 1 if a[i][n-2] == "-" else a[i][n-2] + 1 if a[i][n-2] != "*" else "*"
if a[0][0] == "*":
    a[0][1] = 1 if a[0][1] == "-" else a[0][1] + 1 if a[0][1] != "*" else "*"
    a[1][0] = 1 if a[1][0] == "-" else a[1][0] + 1 if a[1][0] != "*" else "*"
    a[1][1] = 1 if a[1][1] == "-" else a[1][1] + 1 if a[1][1] != "*" else "*"
if a[0][n-1] == "*":
    a[0][n-2] = 1 if a[0][n-2] == "-" else a[0][n-2] + 1 if a[0][n-2] != "*" else "*"
    a[1][n-1] = 1 if a[1][n-1] == "-" else a[1][n-1] + 1 if a[1][n-1] != "*" else "*"
    a[1][n-2] = 1 if a[1][n-2] == "-" else a[1][n-2] + 1 if a[1][n-2] != "*" else "*"
if a[n-1][0] == "*":
    a[n-1][1] = 1 if a[n-1][1] == "-" else a[n-1][1] + 1 if a[n-1][1] != "*" else "*"
    a[n-2][0] = 1 if a[n-2][0] == "-" else a[n-2][0] + 1 if a[n-2][0] != "*" else "*"
    a[n-2][1] = 1 if a[n-2][1] == "-" else a[n-2][1] + 1 if a[n-2][1] != "*" else "*"
if a[n-1][n-1] == "*":
    a[n-1][n-2] = 1 if a[n-1][n-2] == "-" else a[n-1][n-2] + 1 if a[n-1][n-2] != "*" else "*"
    a[n-2][n-1] = 1 if a[n-2][n-1] == "-" else a[n-2][n-1] + 1 if a[n-2][n-1] != "*" else "*"
    a[n-2][n-2] = 1 if a[n-2][n-2] == "-" else a[n-2][n-2] + 1 if a[n-2][n-2] != "*" else "*"
for i in range(n):
    print("".join([str(j) for j in a[i]]))