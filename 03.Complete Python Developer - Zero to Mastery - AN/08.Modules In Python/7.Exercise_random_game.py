import sys
import random

print("******** Welcome to Random Number Guessing Game *********")
start_number = sys.argv[1]
end_number = sys.argv[2]

try:
    rand_number = random.randint(int(start_number), int(end_number))
    result = False
    while not result:
        try:
            user_guess = int(input(f"Please enter your guess number between {start_number} and {end_number}: "))
            if user_guess > rand_number:
                print("Your guess number is too high.")
            elif user_guess < rand_number:
                print("Your guess number is too low.")
            else:
                result = True 
                print(f"Awesome. The correct number is {rand_number}")
        except Exception:
            continue
except Exception as e:
    print("You have provided invalid numbers. Please start the game again.")


# Testing (How to play - run in terminal)
# arguments : start and end numbers for generating random numbers
# python  7.Exercise_random_game.py 1 10