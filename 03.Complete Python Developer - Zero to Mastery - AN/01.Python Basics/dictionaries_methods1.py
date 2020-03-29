user ={
    'name':"richard",
    'weapons':["sword","gun"]
}

print(user['name'])

#this cause key error as the key "age" doesn't exist. To avoid this, we can use get() method.
# print(user['age'])

#get() method will return None if the key doesn't exist.
#we should use it when we are unsure about what key are included in specific dictionary
print(user.get('age'))

#get() with default value
#if key doesn't exist, return default value
#else return the value for that key
print(user.get('age',55))

user2 = dict(name="John")
print(user2)