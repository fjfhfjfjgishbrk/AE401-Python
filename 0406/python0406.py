#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:17:02 2020

@author: fdbfvuie
"""

import math

"""
for i in range(9):
    for j in range(9):
        if j<i:
            print("",end="\t")
        else:   
            print(str(j + 1) + "x" + str(i + 1) + "=" + str((j+1)*(i+1)),end=" \t")
    print("\n")
"""

"""
repeatNum = int(input("Number: "))
numList = [1, 1]
print(1)
print(1)
for i in range(repeatNum - 2):
    numList.append(numList[i] + numList[i + 1])
    print(numList[i + 2])
"""

"""
repeatNum = int(input("Number: "))
numList = [1, 1]
numSum = 0;
for i in range(repeatNum - 2):
    numList.append(numList[i] + numList[i + 1])
    numSum += numList[i + 2] / numList[i + 1]
print(numSum)
"""

"""
num = input("type a 5 digit number: ")
isSame = True
for i in range(len(num) // 2):
    if num[i] == num[-i - 1]:
        continue
    else:
        isSame = False
if isSame:
    print("是回文數")
else:
    print("不是回文數")   
"""

"""
num = input("type a number: ")
numCubeSum = 0
for i in num:
    numCubeSum += int(i) ** 3
if int(num) == numCubeSum:
    print("是水仙花數")
else:
    print("不是水仙花數")
""" 

"""
num = int(input("type a number: "))
triangle = [[] for i in range(num)]
triangle[0].append(1)
print(triangle[0][0], end="\n")
for i in range(num - 1):
    triangle[i + 1].append(1)
    print(triangle[i + 1][0], end="\t")
    for j in range(i):
        triangle[i + 1].append(triangle[i][j + 1] + triangle[i][j])
        print(triangle[i + 1][j + 1], end="\t")
    triangle[i + 1].append(1)
    print(triangle[i + 1][len(triangle[i + 1]) - 1], end="\n")
"""

#"""
num = input("type a b c:")
abc = [int(i) for i in num.split(" ")]
ans = [0, 0]
if abc[1] ** 2 - 4 * abc[0] * abc[2] < 0:
    print("No real root")
else:
    d = int(math.sqrt(abc[1] ** 2 - 4 * abc[0] * abc[2]))
    ans[0] = (-abc[1] + d) / (2 * abc[0])
    ans[1] = (-abc[1] - d) / (2 * abc[0])
    ans.sort(reverse=True)
    if d == 0:
        print("Two same roots x=" + str(int(ans[0])))
    else:
        print("Two different roots x1=" + str(int(ans[0])) + " , x2=" + str(int(ans[1])))
#"""


"""
num = input("type a b c:")
num = num.split(" ")
roots = np.roots([int(i) for i in num])
if roots[0] == roots[1]:
    print("Two same roots x=" + str(int(roots[0])))
elif np.isrealobj(roots):
    print("Two different roots x1=" + str(int(roots[0])) + " , x2=" + str(int(roots[1])))
else:
    print("No real root")
"""

"""
import sys
while 1:
    text = sys.stdin.readline()
    if text == "":
        break
    for i in text:
        print(chr(ord(i)-7),end="")
    print("",end="\n")
"""