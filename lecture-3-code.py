#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 16:38:54 2020

@author: Ellie
"""

import math
# Code / Practice from MIT 6.0001 (OCW)

# Reading Ch. 3

#Find the cube root of a perfect cube
x = int(input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x, 'is', ans)
    
# Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user. If no such pair of integers exists, it should print a message to that effect.

num = int(input("Enter an integer: "))

for power in range(1,6):
    a = (num ** (1.0/power))
    if math.ceil(a) == a:
        print (int(a),',',power)