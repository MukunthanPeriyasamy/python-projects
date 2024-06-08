import random

# User move.
player_input = input("Enter your move rock or paper or scissor: ")
player_move = player_input.lower()
# Generating computer move

random_number = random.randint(1, 3)
computer_move = ""
computer_play = random_number
if computer_play == 1:
    computer_move = "rock"
elif computer_play == 2:
    computer_move = "paper"
else:
    computer_move = "scissor"
print(f"computer move is: {computer_move}")

# Implementing game logic

if player_move == computer_move:
    print("Match Draw!")
elif player_move == 'rock' and computer_move == 'scissor':
    print("You Win!")
elif player_move == "scissor" and computer_move == 'paper':
    print("You Win!")
elif player_move == "paper" and computer_move == 'rock':
    print('You Win!')
else:
    print("Computer Win! You Lost!")


# Rock-Paper-Scissors Game Documentation

## Overview
# This program simulates a game of Rock-Paper-Scissors between a user and the computer.
# The user inputs their move, and the computer randomly generates its move.
# The program then determines the winner based on the rules of Rock-Paper-Scissors and displays the result.
#
# ## How to Use
# 1. **User Input**: The user is prompted to enter their move by typing "rock", "paper", or "scissor".
# 2. **Computer Move**: The computer generates its move randomly.
# 3. **Game Logic**: The program compares the user's move and the computer's move to determine the winner.
# 4. **Result Display**: The result of the game is displayed, indicating whether the user won, lost, or if the game was a draw.
#
# ## Code Breakdown
#
# ### User Input
# ```
# player_input = input("Enter your move rock or paper or scissor: ")
# player_move = player_input.lower()
# ```
# - The user is prompted to enter their move.
# - The input is converted to lowercase to ensure consistency in comparison.
#
# ### Computer Move Generation
# ```
# import random
#
# random_number = random.randint(1, 3)
# computer_move = ""
# computer_play = random_number
# if computer_play == 1:
#     computer_move = "rock"
# elif computer_play == 2:
#     computer_move = "paper"
# else:
#     computer_move = "scissor"
# print(f"computer move is: {computer_move}")
# ```
# - A random number between 1 and 3 is generated.
# - Based on the random number, the computer's move is assigned to either "rock", "paper", or "scissor".
# - The computer's move is displayed.
#
# ### Game Logic
# ```
# if player_move == computer_move:
#     print("Match Draw!")
# elif player_move == 'rock' and computer_move == 'scissor':
#     print("You Win!")
# elif player_move == "scissor" and computer_move == 'paper':
#     print("You Win!")
# elif player_move == "paper" and computer_move == 'rock':
#     print('You Win!')
# else:
#     print("Computer Win! You Lost!")
# ```
# - The user's move is compared with the computer's move.
# - If both moves are the same, the game is a draw.
# - The winning combinations for the user are checked and printed if applicable.
# - If none of the winning conditions for the user are met, the computer wins.
#
# ## Example Run
# ```
# Enter your move rock or paper or scissor: rock
# computer move is: paper
# Computer Win! You Lost!
# ```
# In this example, the user enters "rock", and the computer randomly selects "paper". According to the game rules, paper beats rock, so the computer wins.
#
# ## Key Concepts
# - **Random Number Generation**: `random.randint(1, 3)` is used to generate a random move for the computer.
# - **Conditional Statements**: `if-elif-else` statements are used to determine the game result.
# - **User Input Handling**: Ensures the input is case-insensitive by converting it to lowercase.
#
# ## Dependencies
# - Python standard library (specifically, the `random` module).
#
# ## Notes
# - The game expects correct spelling of "rock", "paper", or "scissor". Any deviation from these inputs will not be handled and may result in unexpected behavior.
# - The game logic adheres to the standard rules of Rock-Paper-Scissors:
#   - Rock beats Scissor
#   - Scissor beats Paper
#   - Paper beats Rock