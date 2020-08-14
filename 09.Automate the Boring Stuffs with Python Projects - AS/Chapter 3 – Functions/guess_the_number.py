import random
number = random.randint(1, 20)

name = input("Hello. What is your name? ")
print(f"Well..{name}, I am thinking of a number between 1 and 20.")

count = 0
correct_guess = False

while True and count < 6:
    try:
        guess = int(input("Take a guess: "))
        if guess > number:
            print("Your guess is too high.")
        elif guess < number:
            print("Your guess is too low.")   
        else:
            print(f"That's correct. The number I was thinking of was {number}.")
            correct_guess = True
            break
        count += 1
    except Exception:
        print("You didn't provide the valid number!")
        continue

if not correct_guess:
    print(f"Thanks for playing. The number I was thinking of was {number}.")