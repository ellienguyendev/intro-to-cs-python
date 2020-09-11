#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 22:06:34 2020

@author: Ellie
"""

# Code from Chapter / Lecture 5

import factR
import fib

# Higher Order Functions and built-in functions

def applyToEach(L,f):
    """ Assumes L is a list, f a function
        Mutates L by replacing each element, e, of L by f(e)"""
    
    for i in range(len(L)):
        L[i] = f(L[i])
        
L = [1, -2, 3.33]

applyToEach(L, abs)
# Apply abs to each element of L --> [1, 2, 3.33]

applyToEach(L, int)
# Apply int to each element of L --> [1, 2, 3]

applyToEach(L, factR)
# Apply factorial to each element of L --> [1, 2, 6]

applyToEach(L, fib)
# Apply Fibbonaci to each element of L --> [1, 2, 13]


# Map

# Maps through these two lists and returns the smaller value at each index
L1 = [1,28,36]
L2 = [2,57,9]
for i in map(min,L1,L2):
    print(i)
    
# Lamda expressions

# Appends x (from first list) to the power of y (from second list) using an anonymous function
L = []
for i in map(lambda x,y: x**y, [1,2,3,4], [3,2,1,0]):
    L.append(i)
print(L)