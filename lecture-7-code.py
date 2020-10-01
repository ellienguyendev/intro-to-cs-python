#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ellie
"""

# Practice Problems and Exercises from Lecture 7

# Finger exercise: Implement a function that meets the specification below. Use a try-except block.

def sumDigits(s):
    """Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5"""
    
    myList = list(s)
    sum = 0
    
    for e in myList:
        try: 
            num = int(e)
            sum += num
        except:
            print('letters and special characters are disregarded')
    return sum
    

sumDigits('h2l3l1o')


# Finger Exercise: Implement a function that satisfies the specification

def findAnEven(L):
    """Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even number"""
  
    for e in L:
        if e % 2 == 0:
            return e
        else:
            raise ValueError('no even number found')
        
findAnEven([1,3,5,7])