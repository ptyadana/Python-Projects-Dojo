user ={
    'name':"richard",
    'weapons':["sword","gun"]
}

print('age' in user)
print('weapons' in user)
print('richard' in user)

#check keys only
print("-----------------")
print('age' in user.keys())

#check values only
print("-----------------")
print('richard' in user.values())

#items
print("-----------------")
print(user.items())

#clear
print("-----------------")
user.clear()
print(user)


#copy
user ={
    'name':"richard",
    'weapons':["sword","gun"]
}

user2 = user.copy()
user.clear()

print("-----------------")
print(user)
print(user2)

#pop
user2.pop('name')
print(user2)

#add new items
user2['age'] = 20
print(user2)

#update
user2.update({'address': '120,NY'})
print(user2)