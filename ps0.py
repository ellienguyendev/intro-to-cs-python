#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 15:33:17 2020

@author: Ellie
"""

# Write a program that does the following in order:
# 1. Asks the user to enter a number “x” 
# 2. Asks the user to enter a number “y”
# 3. Prints out number “x”, raised to the power “y”. 
# 4. Prints out the log (base 2) of “x”.

# Users should see: 
# Enter number x: 2 
# Enter number y: 3 
# x**y = 8
# log(x) = 1

import numpy

x = int(input('Enter number x: '))
y = int(input('Enter number y: '))

print('x**y = {}'.format(x**y))
print('log(x) = {}'.format(numpy.log2(x)))