# Two nested loops are O(n^2)

my_favourite_desserts = ["chocolate", "ice cream", "crackers"]
quantities = [10, 20, 30]

for item in my_favourite_desserts:
    for q in quantities:
        print(item, " - ", q)