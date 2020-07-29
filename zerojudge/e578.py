#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:21 2020

@author: fdbfvuie
"""

A = {}
A['2']='`'
A['3']='1'
A['4']='2'
A['5']='3'
A['6']='4'
A['7']='5'
A['8']='6'
A['9']='7'
A['0']='8'
A['-']='9'
A['=']='0'
A['e']='q'
A['r']='w'
A['t']='e'
A['y']='r'
A['u']='t'
A['i']='y'
A['o']='u'
A['p']='i'
A['[']='o'
A[']']='p'
A['\\']='['
A['d']='a'
A['f']='s'
A['g']='d'
A['h']='f'
A['j']='g'
A['k']='h'
A['l']='j'
A[';']='k'
A['\'']='l'
A['c']='z'
A['v']='x'
A['b']='c'
A['n']='v'
A['m']='b'
A[',']='n'
A['.']='m'
A['/']=','
while 1:
    try:
        a = input()
        for i in a:
            if i in A:
                print(A[i], end="")
            else:
                print(i, end="")
        print()
    except:
        break