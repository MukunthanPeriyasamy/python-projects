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

