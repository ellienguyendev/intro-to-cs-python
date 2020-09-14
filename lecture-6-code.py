#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ellie
Lecture 6 Code and Practice Exercises
"""

def fib(n):
    """Assume n int >= 0
        Return Fibonacci of n"""

    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib(6)

# Finger exercise: When the implementation of fib in Figure 4.7 is used to compute fib(5), how many times does it compute the value of fib(2) on the way to com- puting fib(5)?

count = 0

def fib(n):
    """Assume n int >= 0
        Return how many times fib(2) is computed on the way
        to computing fib(n)"""
    global count
    if n == 0 or n == 1:
        return 1
    else:
        fib(n-1) + fib(n-2)
        if n == 2:
            count += 1

        return count

fib(5)

# Check if a string is a palindrome

def isPalindrom(s):
    """ Assumes s is a str
        Returns True if s is a palindrome; False otherwise.
        Puncuation marks, blanks, and capitilizations are ignored"""

    def toChar(s):
        """ Returns s as a str with no characters other than lowercase letters"""
        s = s.lower
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuv':
                letters = letters + c
        return letters

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[1] and isPal(s[1:-1])

    return isPal(toChar(s))
