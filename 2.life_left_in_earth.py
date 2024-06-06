name=input("Enter your name: ")
age=int(input("Enter your age: "))

#calculating remaining life time
#if we live for 90 years

time_period= 90 - age

#There are 52 weeks in a year 
weeks_left = time_period * 52

print(f"{name}! you have {weeks_left} left. Enjoy every second !!")