#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 6 10:32 2020

@author: fdbfvuie
"""

a = [["Medium Wac", 4], ["WChicken Nugget", 8], ["Geez Burger", 7], ["ButtMilk Crispy Chicken", 6], ["Plastic Toy", 3]]
b = [["German Fries", 2], ["Durian Slices", 3], ["WcFurry", 5], ["Chocolate Sunday", 7]]
total = 0
while True:
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        c = int(input()) - 1
        total += a[c][1]
        print(a[c][0], a[c][1])
    elif n == 2:
        c = int(input()) - 1
        total += b[c][1]
        print(b[c][0], b[c][1])
print("Total: {}".format(str(total)))