#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ellie
Lecture 6 Code and Practice Exercises
"""

# Factorials

# Iterative Factorial

def factI(n):
    """Assumes n an int > 0 
       Returns n!"""
       
    result = 1
    while n > 1:
        result *= n 
        n -= 1
    return result
        
# Recursive Factorial
def factR(n):
    """Assume n an int > 0 
       Returns n!"""
       
    if n == 1:
        return n
    else:
        return n*factR(n-1)

# Fibonacci Sequence

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

# Fibonacci using dictonaries 

def fib_efficient(n, d):
    """Assume n int >= 0
       Assume d dict n: fibonacci of n as key: value pairs
        Return Fibonacci of n"""
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d)+fib_efficient(n-2, d)
        d[n] = ans
        return ans
        
d = {1:1, 2:2}

argToUse = 34
print(fib_efficient(argToUse, d))


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

# Evaluate the lyrics of a song and create a dictionary with how many times each word appears in the song. Then create another function that outputs the most frequent words. Then create a function that outputs how often a word appears a minimum number of times.

lyric_string = "were just ordinary people we dont know which way to go cause were ordinary people maybe we should take it slow take it slow ohh this time well take it slow take it slow, ohh this time well take it slow"

lyrics_list = lyric_string.split()

def lyrics_to_dict(lyrics):
    """"Assume lyrics a list with strings with no special        characters
        Return dictionary with every unique word: how many times it appears in the lyrics"""
    
    myDict = {}
    
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

lyrics_to_dict(lyrics_list)


def most_common_words(freqs):
    """"Assume freqs a dictionary with words: frequency appeared in a song as the key: value pairs
        Return most common words"""
    
    values = freqs.values()
    highest = max(values)
    words = []
    
    for k in freqs:
        if freqs[k] == highest:
            words.append(k)
    return (words, highest)

most_common_words(lyrics_to_dict(lyrics_list))


def words_often(freqs, minTimes):
    """"Assume freqs a dictionary with words: frequency appeared in a song as the key: value pairs
        Assume int > 0
        Return words that appear >= minTimes"""
        
    result = []
    done = False
    
    while not done:
        temp = most_common_words(freqs)
        print(temp)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result
    
words_often(lyrics_to_dict(lyrics_list), 4)


# Towers of Hanoi

def printMove(fr,to):
    print('move from ' + str(fr) + ' to ' + str(to))
    
def Towers(n,fr,to,spare):
    if n == 1:
        printMove(fr,to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
        
Towers(4, 'original', 'destination', 'spare')


# Iterative solution for multiplication

def multI(a,b):
    result = 0 
    
    while b > 0:
        result +=a
        b -= 1
    return result

multI(4,6)

# Recursive solution for multiplication

def multR(a,b):
    if b == 1:
        return a
    else:
        return a + multR(a, b-1)

multR(4,6)

