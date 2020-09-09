#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ellie
"""

# Code / Practice from MIT 6.0001 (OCW)

# Reading Ch. 4

# Write a function isIn that accepts two strings as arguments and returns True if either string occurs anywhere in the other, and False otherwise. Hint: you might want to use the built-in str operation in.

def isIN (string_1, string_2):
    if string_1 in string_2 or string_2 in string_1:
        return True
    else:
        return False
    
isIN('hell', 'hello')