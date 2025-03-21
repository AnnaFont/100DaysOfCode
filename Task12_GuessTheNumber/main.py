# Scope concept
# print(f" print: {variable}")
# Guess the number
# Use mayus when it is a constant

# try:
# code
#except ValueError:

import random

print("Welcome to the number guess. Guess a number between 1 and 100")
num_to_guess = random.randint(1, 100)
game_type = input("Write 'e' for easy or 'h' for hard game: ")
num_attempts = 10
if game_type == 'h':
    num_attempts = 5
print(f" You have {num_attempts} attempts")
game_finished = False
user_num = int(input("Make a guess: "))
while not game_finished:
    if user_num == num_to_guess:
        game_finished = True
        print(f" You rocked it! The number was {num_to_guess}")
    elif num_attempts == 1:
        print("No attempts left... Go home please")
    else:
        num_attempts = num_attempts - 1
        if user_num > num_to_guess:
            print("Too high.")
        else:
            print("Too low.")
        print(f"You have {num_attempts} attempts remaining to guess the number.")
        user_num = int(input("Guess again: "))



