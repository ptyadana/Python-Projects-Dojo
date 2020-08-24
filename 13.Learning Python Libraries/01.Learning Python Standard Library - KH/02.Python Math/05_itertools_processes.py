# Itertools
import itertools

# Infinite Counting
for x in itertools.count(50, 5): # count as 50, 55, 60... infinitely
    print(x)
    if x == 80: # stopper condition
        break


# Infinite Cycling
counter = 0
for c in itertools.cycle("Apple Is so wonderful!"):
    print(c)
    
    counter += 1
    if counter > 50:
        break
    
    
# Infinite Cycling for number
counter = 0
for c in itertools.cycle([1,2,3,4,5]):
    print(c)
    
    counter += 1
    if counter > 50:
        break
    
    
# Infinite Repeating
counter = 0
for r in itertools.repeat("moon!"):
    print(r)
    
    counter += 1
    if counter > 50:
        break 