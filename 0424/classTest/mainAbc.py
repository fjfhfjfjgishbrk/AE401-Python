#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:18:46 2020

@author: fdbfvuie
"""

import abcde

apple = abcde.people("Apple", 250, 35)
print(apple.name, "bmi:", apple.bmi())

peopleApple = abcde.apple("People", 35, 250, 10)
print(peopleApple.name, "bmi:", peopleApple.bmi())
print(peopleApple.name, "volume:", peopleApple.volume())

circleApple = abcde.circle("Circle", 100, 100, 20)
print(circleApple.name, "bmi:", circleApple.bmi())
print(circleApple.name, "volume:", circleApple.volume())
print(circleApple.name, "area:", circleApple.area())