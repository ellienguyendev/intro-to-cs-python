#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ellie
MIT 6.0001 pSet 1c
"""

# In Part B, you had a chance to explore how both the percentage of your salary that you save each month and your annual raise affect how long it takes you to save for a down payment.  This is nice, but suppose you want to set a particular goal, e.g. to be able to afford the down payment in three years. How much should you save each month to achieve this?  In this problem, you are going to write a  program to answer that question.  To simplify things, assume:
# 1. Your semi­annual raise is .07 (7%)
# 2. Your investments have an annual return of 0.04 (4%)  
# 3. The down payment is 0.25 (25%) of the cost of the house 
# 4. The cost of the house that you are saving for is $1M.
# You are now going to try to find the best rate of savings to achieve a down payment on a $1M house in 
# 36 months. Since hitting this exactly is a challenge, we simply want your savings to be within $100 of the required down payment
 
# User inputs their annual salary
annual_salary = float(input('Enter your annual salary: '))

# Variables representing information provided in problem above
total_cost = 1000000.00

portion_down_payment = total_cost * 0.25

semi_annual_raise = .07

annual_return_percentage = 0.04/12

# Range that current savings could be in of down payment
epsilon = 100

# Range for bisection search
low = 0

high = 10000

ans = (low + high)/2.0

# Number of months user has been saving so far
months = 0 

# Number of guesses / iterations before answer was found
numGuesses = 0

# Keep track of how much the user has saved so far
current_savings = 0

# This loop executes until user is within $100 needed for the down payment
while portion_down_payment - current_savings >= epsilon:
    months += 1
    numGuesses += 1
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
    
    monthly_salary = annual_salary/12
    current_savings += monthly_salary
    
    # Bisection search. Guesses the answer to be half of the low - high range to find the best percentage to save in order to pay down payment within 36 months. Low or high is changed depending on if the guess is too high or too low, decreasing the search by half with each iteration.
    if (ans/10000) * monthly_salary * 36 < portion_down_payment:
        low = ans
    else:
        high = ans
    ans = (low + high)/2.0

# If the user is not able to save enough for their down payment within 3 years, display a message. If yes, display the best savings rate and number of steps (guesses) in bisection search
if (ans/10000 == 1.0):
    print('It is not possible to pay the down payment in three years.')
else:
    print('Best savings rate:', round(ans/10000,4))
    print('Steps in bisection search:', numGuesses)