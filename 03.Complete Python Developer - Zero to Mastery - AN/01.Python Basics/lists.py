list1 = ["a","b","c"]
list2 = [1,2,3]
list3 = ["A",2,"CDCC",10,True,"BBB",False]

amazon_cart = [
    "pens",
    "notbooks",
    "shampoo",
    "toothbrush"
]

print(amazon_cart)
print(amazon_cart[0::2])

amazon_cart [1] = "laptop"

print(amazon_cart)
print(amazon_cart[0:3])

print("-----------------------------")

print(amazon_cart)
new_cart = amazon_cart
new_cart[0] = "icecream"

print("--------After pointing newcart to amazon cart---------------------")
print(amazon_cart)
print(new_cart)

#to avoid original list item gets changed, we need to use the copy of original list
print("--------After copying amzon cart to newcart ---------------------")
new_cart = amazon_cart[:]
new_cart[0] = "Vitamin"
print(amazon_cart)
print(new_cart)

a,b,c = ["A","B","C"]
print(a)
print(b)
print(c)