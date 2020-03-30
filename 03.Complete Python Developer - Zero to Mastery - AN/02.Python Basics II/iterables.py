#iterable: string, list, dictionary, tuple, sets
#iterate: one by one checking each item in the collection.

user = {
    'name':'deadpool',
    'age':45,
    'power':'immortality'
}

for key,value in user.items():
    print(f"key: {key} and value : {value}" )

for key in user.keys():
    print(key)

for value in user.values():
    print(value)