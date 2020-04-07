#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 10:01:20 2020

@author: fdbfvuie
"""

import random

"""
#輸入數字
num1 = input("請輸入一個數字: ")
num2 = input("請輸入一個數字: ")
operation = input("1) ➕  2) 減 3) 乘 4) ➗  ")

try:
    #轉換型態
    num1 = int(num1)
    num2 = int(num2)
    operation = int(operation)
    
    #計算
    print("\n")
    if operation == 1:
        print(num1 + num2)
    elif operation == 2:
        print(num1 - num2)
    elif operation == 3:
        print(num1 * num2)
    elif operation == 4:
        print(num1 / num2)
    else:
        print("輸入錯誤")

#例外處理
except ValueError:
    print("輸入錯誤")
"""

"""
#輸入數字
num1 = input("請輸入一個數字: ")

try:
    #轉換型態
    num1 = int(num1)
    
    #計算餘數
    if num1 % 15 == 0:
        print("3和5的倍數")
    elif num1 % 3 == 0:
        print("3的倍數")
    elif num1 % 5 == 0:
        print("5的倍數")
    else:
        print("都不是")

#例外處理
except ValueError:
    print("輸入錯誤")
"""

"""
#輸入數字
side1 = input("第一個邊長: ")
side2 = input("第二個邊長: ")
side3 = input("第三個邊長: ")

try:
    #轉換型態
    side1 = int(side1)
    side2 = int(side2)
    side3 = int(side3)
    
    #判斷任兩邊和有無大於第三邊
    if (side1 + side2 > side3 and side3 + side2 > side1 and side1 + side3 > side2):
        print("\n可圍成三角形")
        
        #找出最大邊
        bigSide = 0
        if side1 > side2:
            bigSide = side1
        else:
            bigSide = side2
        if side3 > bigSide:
            bigSide = side3
            
        #判斷為哪種三角形
        squareSum = side1**2 + side2**2 + side3**2 
        bigSide = bigSide**2
        if squareSum > 2 * bigSide:
            print("銳角三角形")
        elif squareSum == 2 * bigSide:
            print("直角三角形")
        else:
            print("鈍角三角形")
        
    else:
        print("不可圍成三角形")
  
#輸入數字
except ValueError:
    print("輸入錯誤")
"""

"""
#Input name, weight and height
name = input("Name: ")
weight = float(input("Weight: "))
height = float(input("Height: ")) / 100

#Print name, weight, height and BMI
bmi = round(weight / (height * height), 3)
print("\nName:", name)
print("Weight:", weight, "\nHeight:", height * 100)
print("BMI:", bmi)
if bmi < 18.5:
    print("not fat enough")
elif bmi < 25:
    print('normal')
elif bmi < 28:
    print("fat")
elif bmi < 32:
    print("very very fat")
else:
    print("very very very very very very very fat")
"""

"""
#input age
age = input("age: ")
try:
    age = int(age)
    
    #see if age is big enough to watch
    if age < 0:
        print("type a postitve number")
    elif age < 6:
        print("you cannot watch this")
    elif age < 12:
        print("you need adult to watch")
    else:
        print("you can watch")
      
#if input isnt a number
except ValueError:
    print("type a number")
"""
    
"""
#input number
num = input("Guess a number from 1 - 2: ")

try:
    num = int(num)
    #test if number is same with computer random number
    if num < 1 or num > 2:
        print("type a number from 1 - 2")
    elif num == random.randint(1, 2):
        print("correct")
    else:
        print("wrong")
    
#if input not number
except ValueError:
    print("type a number")
"""


#input selection
num = input("1) Paper 2) scissors 3) stone  ")

try:
    num = int(num)
    #print what player and computer choose
    computerNum = random.randint(1, 3)
    a = ["paper", "scissors", "stone"]
    print("\nYou chose", a[num - 1], "  computer chose",  a[computerNum - 1])
    #see who win
    if (computerNum == num):
        print("draw")
    elif computerNum - num == 1 or computerNum - num == -2:
        print("you lose")
    else:
        print("you win")
    
#if input is not number
except ValueError:
    print("type a number")
 

    
