#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 9 10:32 2020

@author: fdbfvuie
"""

while True:
    try:
        n = int(input())
        nums = []

        for i in range(n):
            nums.append(input().split(" "))
        nums.sort(key=lambda x: (int(x[0]), int(x[1])))

        for i in range(len(nums)):
            print(nums[i][0], nums[i][1])

    except:
        break