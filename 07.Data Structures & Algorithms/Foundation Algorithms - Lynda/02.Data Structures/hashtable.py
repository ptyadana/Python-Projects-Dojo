# demonstrate hashtable usage


#  create a hashtable all at once
item1 = {"key1": 1, "key2": 2, "key3": "three"}
print(item1)

#  create a hashtable progressively
item2 = {}
item2["key1"] = 1
item2["key2"] = 2
item2["key3"] = 3
print(item2)

#  try to access a nonexistent key
print(item1.get("key4"))

#  replace an item
item1["key2"] = "two"
print(item1)

#  iterate the keys and values in the dictionary
for key, value in item2.items():
    print("key: ", key, " , value: ", value)