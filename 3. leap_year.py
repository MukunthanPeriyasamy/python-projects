# Getting input (year) from the user

year = int(input("Enter the year: "))

# The user entered input year is checking using control flow statement
#if the year is divisible by 4 and not divisible by 100  or the year divisible by 400 will be a leap year

if (year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is a leap year")
    print("This year will end up with 366 days!")

# If the above if condition failfs then the year is not a leap year and else part will be executed.
else:
    print(f"{year} is not a leap year")
    print("This year will end up with 365 days!")


# # Leap Year Checker Program Documentation
#
# ## Introduction
#
# This program is designed to determine whether a given year is a leap year. It takes an input year from the user and uses control flow statements to check the leap year conditions. The program then outputs whether the year is a leap year and the total number of days in that year.
#
# ## Program Structure
#
# The program consists of the following main components:
#
# 1. **Input Collection**: Collecting the year from the user.
# 2. **Leap Year Condition Check**: Using control flow statements to determine if the year is a leap year.
# 3. **Output**: Displaying the result to the user.
#
# ## Detailed Description
#
# ### 1. Input Collection
#
# The program starts by prompting the user to enter a year. The input is collected as a string and then converted to an integer.
#
# ```
# year = int(input("Enter the year: "))
# ```
#
# ### 2. Leap Year Condition Check
#
# The program checks whether the input year is a leap year using the following conditions:
# - A year is a leap year if it is divisible by 4 and not divisible by 100, or it is divisible by 400.
#
# This is implemented with an if-else statement:
#
# ```
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year")
#     print("This year will end up with 366 days!")
# else:
#     print(f"{year} is not a leap year")
#     print("This year will end up with 365 days!")
# ```
#
# #### Explanation of Conditions
#
# 1. **Divisibility by 4**: `year % 4 == 0`
#    - This condition checks if the year is divisible by 4.
# 2. **Not Divisibility by 100**: `year % 100 != 0`
#    - This condition ensures that the year is not a century year unless it is divisible by 400.
# 3. **Divisibility by 400**: `year % 400 == 0`
#    - This condition checks if the year is a century year that is also divisible by 400.
#
# ### 3. Output
#
# Depending on whether the year meets the leap year conditions, the program prints the appropriate message:
#
# - If the year is a leap year:
#   ```
#   print(f"{year} is a leap year")
#   print("This year will end up with 366 days!")
#   ```
#
# - If the year is not a leap year:
#   ```python
#   print(f"{year} is not a leap year")
#   print("This year will end up with 365 days!")
#   ```
#
# .