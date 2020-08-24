# Random Module
import random

# Random Numbers
print(random.random())

# stimulating coin flips, using randrange()
decider = random.randrange(2) # exclusive of number => 0,1
print("HEAD" if decider == 0 else "TAIL")
print(decider)

# stimulating die roll
print("You rolled a ", random.randrange(1, 7)) # start : inclusive , end : exclusive
print(random.randint(1, 7))

# Random Choices
lotteryWinners = random.sample(range(100), 5) #Sample size of 100, get 5 random numbers
print("lottery winners: ", lotteryWinners)

possiblePets = ["cat", "dog", "rabbit"]
print(random.choice(possiblePets))

# Shuffle
cards = ["King", "Queen", "Ace", "Jack"]
random.shuffle(cards)
print(cards)