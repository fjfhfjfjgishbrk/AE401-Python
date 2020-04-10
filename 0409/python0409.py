#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 10:28:31 2020

@author: fdbfvuie
"""

"""
def operation(oper, n1, n2):
    if oper == 1:
        return n1+n2
    elif oper == 2:
        return n1-n2
    elif oper == 3:
        return n1*n2
    elif oper == 4:
        return n1/n2
    
num1 = input("number 1: ")
num2 = input("number 2: ")
a = input("1 for add, 2 for minus, 3 for 乘法, 4 for division: ")
print(operation(int(a), int(num1), int(num2)))
"""

"""
studentA = {"chinese": 83, "english": 96, "math": 92}
temp = {"social studies": 59, "science": 77}
studentA.update(temp)
print(studentA.keys())
print(studentA.values())
print(studentA.items())
studentA['math'] = 100
del studentA['chinese']
"""

"""
text = input("type something: ")
letters = {}
for i in text:
    letters.setdefault(i, 0)
    letters[i] += 1
for i, j in letters.items():
    print(i ,j)
"""

def f(a):
    print(a + " highest score: " + str(max([i[a] for i in scoreList])))
    print(a +                            " lowest score: " + str(min([i[a] for i in scoreList])))
    print(a + " average score: " + str(sum([i[a] for i in scoreList]) / len(scoreList)))
    print()

scoreList = []
while True:
    stuName = input("type name: ")
    if stuName == "-1":
        break
    scoreList.append({})
    scoreList[-1]["name"] = stuName
    scoreList[-1]["chinese"] = int(input(stuName + " chinese score: "))
    scoreList[-1]["english"] = int(input(stuName + " english score: "))
    scoreList[-1]["math"] = int(input(stuName + " math score: "))
    
for i in scoreList:
    tempList = [i["chinese"], i["english"], i["math"]]
    tempList.sort()
    print(i["name"] + " highest score:" + str(tempList[-1]))
    print(i["name"] + " lowest score:" + str(tempList[0]))
    print(i["name"] + " average score:" + str(round(sum(tempList) / 3, 2)))
    print()

f("chinese")
f("english")
f("math")

import math
while True:
    try:
        n = input().split(" ")
        print(math.gcd(int(n[0]), int(n[1])))
    except:
        break

    
    
