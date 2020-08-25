"""
use Monte Carlo method for simulation which uses random sampling to evaluate possible outcomes.
this program will determine the probability of certain outcomes when rolling dice.

Input: variable number of arguments for sides of dice
Output: table of possible outcome
example: roll_dice(4, 6, 6) => useing 4 side die and two 6 sided dice
"""


import random

def sort_dict(dictionary):
    new_dict = {}
    lst = [k for k in dictionary.keys()]
    lst.sort()
    
    for key in lst:
        new_dict[key] = dictionary[key]
    return new_dict
        
def roll_dice(*args):
    number_of_simulations = int(1e6) # a million times
    sides_tracker = {}
    sum_tracker = {}
    
    for sim in range(number_of_simulations):
        total_sum = 0
        for roll in args:
            side_of_dice = random.randint(1, roll)
            
            # Counting Sides 
            side_count = sides_tracker.get(side_of_dice, 0) + 1   # check and update the counter for each side
            sides_tracker[side_of_dice] = side_count
            
            # Counting sum of dice
            total_sum += side_of_dice
        
        sum_count = sum_tracker.get(total_sum, 0) + 1 
        sum_tracker[total_sum] = sum_count
    
    print("----- OUTCOME PROBABILITY for Each Side -----")
    for key,value in sort_dict(sides_tracker).items():
        probability = (sides_tracker[key] / (number_of_simulations * len(args))) * 100
        print("side {} : {:0.2f}%".format(key, probability))
    
    print("\n----- OUTCOME PROBABILITY for Sum -----")
    for key,value in sort_dict(sum_tracker).items():
        probability = (sum_tracker[key] / number_of_simulations) * 100
        print("{} : {:0.2f}%".format(key, probability))
            
        
if __name__ == "__main__":
    roll_dice(4, 6, 6)
    roll_dice(4, 6, 6, 20)