# Itertools Part 2
import itertools

# Permutations: Order matters - some copies with same inputs but in different order
election = {
    1: "Bob",
    2: "Karren",
    3: "Erin",
}

for p in itertools.permutations(election):
    print(p)
    
for p in itertools.permutations(election.values()):
    print(p)

print("----------------")

# Combinations: Order does not matter - no copies with same inputs
colors = ["red","blue", "purple", "orange", "pink"]

for c in itertools.combinations(colors, 2): # we want to pick 2 colors out of 3
    print(c)
    
for c in itertools.combinations(colors, 3):
    print(c)
    