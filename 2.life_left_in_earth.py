name=input("Enter your name: ")
age=int(input("Enter your age: "))

#calculating remaining life time
#if we live for 90 years

time_period= 90 - age

#There are 52 weeks in a year 
weeks_left = time_period * 52

print(f"{name}! you have {weeks_left} left. Enjoy every second !!")

------------------------------------------------------------------

#  Program Documentation: Remaining Life Time Calculator

#  Description:
# This Python program calculates the approximate number of weeks left in a person's life based on their current age. It assumes a maximum lifespan of 90 years.

#  Input:
# 1. User enters their name.
# 2. User enters their age.

#  Output:
# The program calculates the remaining life time in weeks and displays a personalized message.

# Algorithm:
# 1. Prompt the user to input their name and age.
# 2. Calculate the remaining years of life by subtracting the user's age from 90.
# 3. Multiply the remaining years by 52 (the number of weeks in a year) to get the total weeks left.
# 4. Display the result along with a friendly message.

#  Example Usage:

#  Enter your name: John
#  Enter your age: 30
#  John! You have 3120 weeks left. Enjoy every second!!
