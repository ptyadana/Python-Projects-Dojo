# Range -> range instance that holds all nums counting by one between 0 and first input
# List -> lists numbers from the inputted tuple

numberedContestants = range(30)

print(list(numberedContestants))

for c in list(numberedContestants):
    print(f"Contestant {c} is here.")

lucky_winners = range(7, 30, 5)
print(list(lucky_winners))