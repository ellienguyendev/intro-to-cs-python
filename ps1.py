#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ellie
MIT 6.0001 pSet 1a
"""

# Write a program that will calculate how many months it will take you to save up for a down payment for your dream home

# User inputs their annual salary, the percentage of their salary they would like to save, and the total cost of their dream home
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))

# The amount to put a down payment on their home (25% of total cost)
portion_down_payment = total_cost * 0.25

# Annual return of 4%, received at the end of each month
annual_return_percentage = 0.04/12

# Monthly salary
monthly_salary = annual_salary/12

# Amount saved monthly by the user, based on the percentage they indicated
monthly_savings = monthly_salary * portion_saved

# Variables to help up keep track of how much the user has saved so far and how many months
current_savings = 0
months = 0

# While loop is executed until the user has saved the amount needed to pay their down payment. Each month we add their monthly savings and the annual return to the current savings. Number of months increments by 1 each iteration.
 
while current_savings <= portion_down_payment:
    current_savings += monthly_savings
    current_savings += current_savings * annual_return_percentage
    months += 1

print(months)