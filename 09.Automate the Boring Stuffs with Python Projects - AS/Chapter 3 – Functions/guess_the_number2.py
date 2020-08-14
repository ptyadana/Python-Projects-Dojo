#using for loop

import random
number = random.randint(1, 20)

name = input("Hello. What is your name? ")
print(f"Well..{name}, I am thinking of a number between 1 and 20.")

for guess_taken in range(1,7):
    try:
        guess = int(input("Take a guess: "))
        if guess > number:
            print("Your guess is too high.")
        elif guess < number:
            print("Your guess is too low.")   
        else:
            break
    except Exception:
        print("You didn't provide the valid number!")
        continue

if guess == number:
    print(f"Great Job..{name}! You gussed the number in {guess_taken} times.")
else:
    print(f"Thanks for playing. The number I was thinking of was {number}.")