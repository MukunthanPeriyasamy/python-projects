import random


def play_game(attempts):
    computer_choice = random.randint(0, 100)
    for _ in range(attempts):
        print(f"You Have {attempts} attempts. Keep Count")
        make_guss = int(input("Make a guss: "))
        if make_guss == computer_choice:
            print(f"You got it!. The number is {computer_choice}")
            return
        elif make_guss < computer_choice:
            print("Too low")
        elif make_guss > computer_choice:
            print("Too high")
        attempts -= 1
    print("You lost all attempts.")


easy_or_hard = input("Choose your difficulty. Type 'easy' or 'hard' :").lower()
if easy_or_hard == "easy":
    play_game(10)
elif easy_or_hard == "hard":
    play_game(5)
else:
    print("Invalid choice")
