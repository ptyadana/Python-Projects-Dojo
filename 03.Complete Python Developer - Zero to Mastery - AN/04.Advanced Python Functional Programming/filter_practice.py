items = [12, 1, 7, 5, 4, 2, 9]

def less_than_five(x):
    return x < 5

#need to convert to list
new_items = list(filter(less_than_five, items))

print(new_items)