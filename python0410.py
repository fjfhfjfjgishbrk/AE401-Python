#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 10:34:31 2020

@author: fdbfvuie
"""


import random

word = {'apple': '蘋果', 'banana': '香蕉', 'cat': '貓', 'dog': '狗'}
while True:
    a = int(input("type 1 for word list, 2 for english to chinese, 3 to add new words, 4 for chinese to english, 5 for test, -1 to quit: "))
    if a == 1:
        print("word list: ")
        for i, j in word.items():
            print(i, j)
    elif a == 2:
        print("english to chinese: ")
        while True:
            print("type -1 to exit")
            eWord = input("type english word: ")
            if eWord in word:
                print(word[eWord])
            elif eWord == "-1":
                break
            else:
                print("not in dictionary")
    elif a == 3:
        print("add new words: ")
        while True:
            print("type -1 to exit")
            addE = input("add english word: ")
            if addE == "-1":
                break
            else:
                addC = input("chinese word: ")
                word[addE] = addC
                print(addE + " and " + addC + " added")
    elif a == 4:
        print("chinese to english: ")
        while True:
            print("type 1 to exit")
            cWord = input("type chinese word: ")
            if cWord == "1":
                break
            elif cWord == "-1":
                continue
            isIn = False
            for i, j in word.items():
                if j == cWord:
                    print(i)
                    isIn = True
                    break
            if not isIn:
                print("not in dictionary")
    elif a == 5:
        print("test: ")
        n = int(input("how many questions: "))
        correct = 0
        wordKey = [i for i in word.keys()]
        wordValue = [i for i in word.values()]
        for i in range(n):
            rand = random.randint(0, len(word) - 1)
            if random.random() < 0.5:
                ans = input("whats the chinese of " + wordKey[rand] + ": ")
                if ans == wordValue[rand]:
                    print("correct")
                    correct += 1
                else:
                    print("wrong, correct answer: " + wordValue[rand])
            else:
                ans = input("whats the english of " + wordValue[rand] + ": ")
                if ans == wordKey[rand]:
                    print("correct")
                    correct += 1
                else:
                    print("wrong, correct answer: " + wordKey[rand])
            print("correct: " + str(correct) + " / " + str(i + 1))
        print("test end")
    elif a == -1:
        break


"""
f = open("a.txt", "a")
txt = f.write("sushdkvjwejkd")
f.close()
"""













