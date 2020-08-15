# program that checks the number of straks (either Heads or Tails)
# in flipping the coins for specific number of times (like 10,000)

import random


def flip_coin(number_of_flips):
    choice = ["H","T"]
    return random.choices(choice, k=number_of_flips)


def check_streaks(records, streaks_rule):
    number_of_streaks = 0
    counter = 0

    streak_checker_item = records[0]
    for item in records[1:len(records)]:
        if item == streak_checker_item:
            counter += 1

            if counter == streaks_rule:
                number_of_streaks += 1
                counter = 0 #reset counter

        else:
            streak_checker_item = item
            counter = 0 #reset counter
            
    return number_of_streaks


def main():
    
    total_expirements = 10000

    for expirement_number in range(total_expirements):

        # Code that creates a list of 100 'heads' or 'tails' values.
        flips_per_expirement = 100
        record_list = flip_coin(flips_per_expirement)
        
        # Code that checks if there is a streak of 6 heads or tails in a row.
        predefined_streak_number = 6
        number_of_streaks = check_streaks(record_list, predefined_streak_number)

    print(f"Number of Streaks: {number_of_streaks}")
    print(f"Chance of streak: {number_of_streaks / 100} %")


if __name__ == "__main__":
    main()

    #testing
#     test_list = ['T', 'H', 'T', 'T', 'H', 'H', 'T', 'T', 'T', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'T', 'T', 'H', 'T', 'H', 'T',
# 'H', 'H', 'T', 'H', 'T', 'T', 'T', 'T', 'H', 'T', 'T', 'H', 'T', 'H', 'T', 'H', 'H', 'T', 'T', 'T', 'H', 'H', 'H', 'T', 'T', 'T', 'H', 'H', 'H', 'H', 'H', 'H', 'T', 'H', 'T', 'T', 'H', 'H', 'T', 'T', 'T', 'H', 'T', 'H', 'T', 'H', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'H', 'T', 'H', 'T', 'T', 'T', 'T', 'T', 'H', 'H', 'H', 'T', 'T', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'T', 'H']
    
#     number_of_streaks = check_streaks(test_list, 6)
#     print(number_of_streaks)