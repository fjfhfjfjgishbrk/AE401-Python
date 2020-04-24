#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:41:26 2020

@author: fdbfvuie
"""

import a

class student():
    def __init__(self, n, Id, c = None, e = None, m = None):
        self.score = a.score(c, e, m)
        self.name = n
        self.__id = Id
        
    def printSelf(self):
        print(self.name)
        print(self.__id)
        print(self.score.average())