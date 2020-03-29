basket = [1,2,3,4,5]
basket.append(100)

new_basket = basket
print(basket)
print(new_basket)

#Adding Items

new_basket.append(200)
print(basket)
print(new_basket)

new_basket = basket[:]
#insert
new_basket.insert(1,300)

print(basket)
print(new_basket)

#extend
new_basket.extend([11,22,33])
print(new_basket)

# Removing Items
#pop
new_basket.pop()
print(new_basket)

#pop with index
new_basket.pop(1)
print(new_basket)

#remove with object
new_basket.remove(200)
print(new_basket)

#clear everything
new_basket.clear()
print(new_basket)

