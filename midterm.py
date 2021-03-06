#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ellie
"""

# *** Problem 1 ***

# 1.1: True
x = "pi"
y = "pie"
x,y = y,x 
print(x,y)

# 1.2: False // if x is less than 3
def f(x):
    while x > 3:
        f(x+1)
f(1)

# 1.3: False // conditionals
    
# 1.4: False // scopes
    
# 1.5: True // loops don't usually run with negative numbers

# 1.6: False 
    
# 1.7: True

# 1.8: False
    
# 1.9: False
def f(x):
    a = []
    while x > 0:
        a.append(x)
        print(id(a))
        f(x-1)
f(2)

# 1.10: True


# *** Problem 2 ***

# 2.1: L maps strings to integers
    
# 2.2: none of the above
    
# 2.3: a list
    
# 2.4: all of the above
    
# 2.5: none of the above


# *** Problem 3 ***

# 3.1
stuff = 'which values will print Found It'
for thing in stuff:
    if thing == "iQ":
        print("Found It")
        
["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"]
("iBoy", "iGirl", "iQ", "iC","iPaid","iPad")
["iQ"]

# 3.2:  Nothing is wrong; the code is fi ne as-is.
def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

Square(6)

# *** Problem 4 ***

# Implement a function called closest_power that meets the speci cations below.
    
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    
    e = 0
    
    while base**e <= num:
        e += 1

    x = abs(num - base**(e-1))
    y = abs(num - base**e)

    if x <= y:
        e -= 1
    
    return e

closest_power(3,12)

# *** Problem 5 ***

# Write a Python function that returns the sum of the pairwise products of listA and listB . You should assume that and have the same length and are two lists of integer numbers. For example, if and , the dot product is 1*4 + 2*5 + 3*6 , meaning your function should return:
# Hint: You will need to traverse both lists in parallel.
# This function takes in two lists of numbers and returns a number.

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    
    result = 0
    
    for i in range(len(listA)):
        result += listA[i] * listB[i]
        
    return result

dotProduct([1,2,3], [4,5,6])

# *** Problem 6 ***

# Implement a function that meets the speci cations below.
    
def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    
    L.reverse()
    
    for e in L:
        e.reverse()
    
deep_reverse([[1,2],[3,4],[5,6,7])

# *** Problem 7 ***

# Helper function (unknown operations. solution must work for all instances of f)

def f(a,b):
    return a + b

def dict_interdiff(d1,d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    
    common = {}
    single = {}
    
    
    for e in d1:
        if e in d2:
            common[e] = f(d1[e], d2[e])
        else:
            single[e] = d1[e]
    
    for i in d2:
        if i not in d1:
            single[i] = d2[i]
    
    return (common,single)

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

dict_interdiff(d1,d2)


# *** Problem 8 ***

# Implement a function that meets the speci cations below.

def f(i):
    return i + 2
def g(i):
    return i > 5

L = [0, -10, 5, 6, -4]

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you.
    f takes in an integer, applies a function, returns another integer
    g takes in an integer, applies a Boolean function,
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    
    for e in L[:]:
        ans = g(f(e))
        if  ans == False:
            L.remove(e)
    
    if len(L) == 0:
        return -1
    
    return max(L)
    
print(applyF_filterG(L, f, g))
print(L)


# *** Problem 9 ***

# Write a function to  atten a list. The list contains other lists, strings, or ints. For example,[[1,'a',['cat'],2],[[[3]],'dog'],4,5]  attened into [1,'a','cat',2,3,'dog',4,5] (order matters)

def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    
    flatList = []
    
    def loop(sublist):
        for item in sublist:
            if isinstance(item, list):
                loop(item)
            else:
                flatList.append(item)
                
    loop(aList)
    
    return flatList
            
flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])