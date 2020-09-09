#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ellie
MIT 6.0001 pSet 1b
"""

# Write a program that will calculate how many months it will take you to save up for a down payment for your dream home
# In ps1b.py, copy your solution to Part A (as we are going to reuse much of that machinery).  Modify your program to include the following
# 1. Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage)
# 2. After the 6th month, increase your salary by that percentage.  Do the same after the 12th month, the 18th month, and so on. 

# User inputs their annual salary, the percentage of their salary they would like to save, their smi annual salary raise, and the total cost of their dream home
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
semi_annual_raise = float(input('Enter the percent of your semi annual salary raise: '))
total_cost = float(input('Enter the cost of your dream home: '))

# The amount to put a down payment on their home (25% of total cost)
portion_down_payment = total_cost * 0.25

# Annual return of 4%, received at the end of each month
annual_return_percentage = 0.04/12

# Variables to help up keep track of how much the user has saved so far and how many months
current_savings = 0
months = 0

# While loop is executed until the user has saved the amount needed to pay their down payment. Each month we add their monthly savings and the annual return to the current savings. Number of months increments by 1 each iteration.
 
while current_savings <= portion_down_payment:
    months += 1
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
    monthly_salary = annual_salary/12
    monthly_savings = monthly_salary * portion_saved
    current_savings += monthly_savings
    current_savings += current_savings * annual_return_percentage

print(months)