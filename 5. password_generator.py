import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
for letter in range(nr_letters):
    random_letter = random.choice(letters)
    password.append(random_letter)
for symbol in range(nr_symbols):
    random_symbol = random.choice(symbols)
    password.append(random_symbol)
for number in range(nr_numbers):
    random_number = random.choice(numbers)
    password.append(random_number)
random.shuffle(password)

new_password = ""
for char in password:
    new_password += char
print(new_password)


# PyPassword Generator Documentation

## Overview
# The PyPassword Generator is a simple Python script designed to create a randomized password based on user specifications.
# Users can specify the number of letters, symbols, and numbers they want in their password, and the script will generate a secure password containing those elements.
#
# ## Features
# - Customizable length for letters, symbols, and numbers.
# - Randomized selection of characters to enhance password security.
# - Output of a securely generated password.
#
# ## Usage
# 1. Run the script.
# 2. Input the desired number of letters when prompted.
# 3. Input the desired number of symbols when prompted.
# 4. Input the desired number of numbers when prompted.
# 5. The script will output a randomized password based on the input criteria.
#
# ## Code Explanation
# 
# ### Imports
# - **random**: This module is used to generate random choices from the specified lists of characters.
#
# ### Character Lists
# - **letters**: A list containing both lowercase and uppercase English letters.
# - **numbers**: A list containing digits from 0 to 9.
# - **symbols**: A list containing special characters often used in passwords.
#
# ### User Input
# - The script prompts the user to input the desired number of letters, symbols, and numbers for their password.
# - It converts user input from strings to integers using `int()`.
#
# ### Password Generation
# - An empty list is initialized to store the random characters.
# - The script uses `for` loops to iterate based on the user-specified number of letters, symbols, and numbers.
#   - **random.choice()**: Selects a random element from the respective list (letters, symbols, or numbers).
#   - Each selected character is appended to the password list.
#
# ### Shuffling and Output
# - **random.shuffle()**: Shuffles the list of selected characters to ensure randomness.
# - The script concatenates the shuffled characters into a single string to form the final password.
# - The final password is printed to the console.