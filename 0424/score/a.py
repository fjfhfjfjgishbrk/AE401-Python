#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:40:50 2020

@author: fdbfvuie
"""


class score():
    
    scoreSum = 0
    scoreNum = 0
    
    def __init__(self, c = None, e = None, m = None):
        self.chinese = c
        self.english = e
        self.math = m
        self.totalScore()
    
    def totalScore(self):
        if self.chinese != None:
            self.scoreSum += self.chinese
            self.scoreNum += 1
        if self.english != None:
            self.scoreSum += self.english
            self.scoreNum += 1
        if self.math != None:
            self.scoreSum += self.math
            self.scoreNum += 1
        
    def average(self):
        return round(self.scoreSum / self.scoreNum, 2)