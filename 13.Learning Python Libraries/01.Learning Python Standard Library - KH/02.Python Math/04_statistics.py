# Statistics Module
import statistics
import random
import math

random.seed(2)
agesData = random.sample(range(10, 50), 10) #get 10 random ages of people ranging from 0, 49
print(agesData)
print(sorted(agesData))

print(statistics.mean(agesData))
print(statistics.median(agesData))
print(statistics.variance(agesData))
print(statistics.stdev(agesData))
print(math.sqrt(statistics.variance(agesData))) # stdev = square root of variance


cookies = [1, 2, 3, 1, 3, 1]
print(statistics.mode(cookies))

