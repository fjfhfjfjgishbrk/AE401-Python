#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:41 2020

@author: fdbfvuie
"""

import codecs
import re
import sys
sys.stdin = codecs.getreader('latin-1')(sys.stdin.detach())
print(sum([len(re.sub('[^A-Za-z0-9 ]', '', line).split()) for line in sys.stdin]))