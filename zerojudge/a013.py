#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 6 10:34 2020

@author: fdbfvuie
"""

a =  {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
b = {"CM": -100, "CD": -100, "XC": -10, "XL": -10, "IX": -1, "IV": -1}
c = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
while True:
    num = input().split(" ")
    if num[0] == "#":
        break
    numbers = [0, 0]
    for j in range(2):
        for i in range(len(num[j])):
            if num[j][i:i+2] in b.keys():
                numbers[j] += b[num[j][i:i+2]]
                i += 1
            else:
                numbers[j] += a[num[j][i]]
    res = abs(numbers[1] - numbers[0])
    if res == 0:
        print("ZERO")
    while res > 0:
        for value, roman in c.items():
            if res - value >= 0:
                print(roman, end="")
                res -= value
                break
    print()