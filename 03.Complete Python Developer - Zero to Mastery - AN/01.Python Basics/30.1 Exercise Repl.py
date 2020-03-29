# using this list, 
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list
basket.remove("Banana")
print(basket)

# 2. Remove "Blueberries" from the list.
basket.remove("Blueberries")
print(basket)

# 3. Put "Kiwi" at the end of the list.
basket.append("Kiwi")
print(basket)

# 4. Add "Apples" at the beginning of the list
basket.insert(0,"Apples")
print(basket)

# 5. Count how many apples in the basket
apple_count = basket.count("Apples")
print(apple_count)

# 6. empty the basket
basket.clear()
print(basket)
