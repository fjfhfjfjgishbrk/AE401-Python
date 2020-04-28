#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 19:56 2020

@author: fdbfvuie
"""

a = {}
n1 = input()
n1 = n1.split(" ")
sum = 0

for i in range(0, len(n1)):
    if n1[i] == "":
        continue
    temp = n1[i].split(":")
    a[temp[0]] = temp[1]

n2 = input().split(" ")
for i in range(0, len(n2)):
    if n2[i] == "":
        continue
    temp = n2[i].split(":")
    if temp[0] in a:
        sum += int(a[temp[0]]) * int(temp[1])

print(sum)