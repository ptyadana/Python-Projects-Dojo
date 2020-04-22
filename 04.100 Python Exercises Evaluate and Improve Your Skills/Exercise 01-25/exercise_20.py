# Question: Calculate the sum of all dictionary values.

d = {"a": 1, "b": 2, "c": 3}

# Expected output: 
#  6 

#Answer:
my_sum=0
for value in d.values():
    my_sum+=value
print(my_sum)

#Answer 2:
d = {"a": 1, "b": 2, "c": 3}
print(sum(d.values()))


# Explanation: 
# d.values()  returns a list-like dict_values  object while the sum  function calculates the sum of the dict_values  items.