#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 10:18 2020

@author: fdbfvuie
"""

while True:
    try:
        a = input().split(" ")
        a = [int(i) for i in a]
        a.sort()

        # 轉換型態
        side1 = int(a[0])
        side2 = int(a[1])
        side3 = int(a[2])
        print(side1, side2, side3)
        # 判斷任兩邊和有無大於第三邊
        if (side1 + side2 > side3 and side3 + side2 > side1 and side1 + side3 > side2):

            # 找出最大邊
            bigSide = 0
            if side1 > side2:
                bigSide = side1
            else:
                bigSide = side2
            if side3 > bigSide:
                bigSide = side3

            # 判斷為哪種三角形
            squareSum = side1 ** 2 + side2 ** 2 + side3 ** 2
            bigSide = bigSide ** 2
            if squareSum > 2 * bigSide:
                print("Acute")
            elif squareSum == 2 * bigSide:
                print("Right")
            else:
                print("Obtuse")

        else:
            print("No")
            
    except:
        break