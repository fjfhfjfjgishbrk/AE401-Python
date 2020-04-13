#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 10:37:34 2020

@author: fdbfvuie
"""

import datetime

"""
peopleNum = int(input("how many people: "))
scoreList = []

for i in range(peopleNum):
    scoreList.append([])
    scoreList[i].append(input("person " + str(i+1) + " name: "))
    scoreList[i].append(int(input("person " + str(i+1) + " score: ")))

scoreList.sort(key = lambda x:x[1])
print("lowest score:", str(scoreList[0][0]),  str(scoreList[0][1]))
print("highest score:", str(scoreList[-1][0]), str(scoreList[-1][1]))
print("average: " + str(sum(i for name,i in scoreList) / peopleNum))
"""

def setApple():
    temp = []
    while True:
        b = int(input("how many apples: "))
        if b < 0:
            print("type a positive number")
        else:
            temp.append(b)
            break
    while True:
        b = int(input("how much per apple: "))
        if b < 0:
            print("type a positive number")
        else:
            temp.append(b)
            break
    return temp


x = datetime.datetime.now()

f = open("apple.txt", "r")
temptxt = []
appleSold = []
for line in f.readlines():
    temptxt.append(line.strip())
f.close()
if len(temptxt) < 3:
    print("setting:")
    setting = setApple()
    apple = setting[0]
    price = setting[1]
else:
    apple = int(temptxt[0])
    price = int(temptxt[1])
    for i in range(2, len(temptxt)):
        appleSold.append(int(temptxt[i]))


while True:
    print("type 1 for setting, 2 for import, 3 for selling, 4 for sum, 5 to see what is left, 6 to search, -1 to end")
    a = int(input("input: "))
    if a == 1:
        print("setting:")
        setting = setApple()
        apple = setting[0]
        price = setting[1]
    elif a == 2:
        print("import:")
        print("type -1 to exit")
        while True:
            appleIn = int(input("import how many apples: "))
            if appleIn ==  -1:
                break
            elif appleIn < 0:
                print("type a positive number")
                continue
            apple += appleIn
            print(str(appleIn) + " apples imported")
    elif a == 3:
        print("sell:")
        print("type -1 to exit")
        while True:
            appleOut = int(input("sell how many apples: "))
            if appleOut == -1:
                break
            elif appleOut < 0:
                print("type a positive number")
                continue
            if appleOut > apple:
                print("there is not enough apple")
            else:
                #appleSold.append([str(x.strftime("%m")) + str(x.strftime("%d")),appleOut])
                appleSold.append(appleOut)
                apple -= appleOut
                print(str(appleOut) + " apples sold")
    elif a == 4:
        print("total:")
        print(str(len(appleSold)) + "筆交易")
        for i in range(len(appleSold)):
            print("第" + str(i + 1) + "筆交易: " + str(appleSold[i]) + "顆蘋果")
        print("total: " + str(sum(appleSold) * price) + " dollars")
    elif a == 5:
        print("apple left")
        print(""*apple)
        #print(apple + " apples")
    elif a == 6:
        print("searcH: ")
        print("type -1 to exit")
        while True:
            appleSearch = int(input("查詢第幾筆交易: "))
            if appleSearch == -1:
                break
            elif appleSearch <= 0:
                print("type a positive number")
                continue
            elif appleSearch > len(appleSold):
                print("no data")
                continue
            print("第" + str(appleSearch) + "筆交易: " + str(appleSold[appleSearch - 1]) + "顆蘋果")
    elif a == -1:
        f = open("apple.txt", "w")
        temptxt = [str(i) for i in appleSold]
        temptxt.insert(0, str(price))
        temptxt.insert(0, str(apple))
        f.write("\n".join(temptxt))
        f.close()
        break
    else:
        continue