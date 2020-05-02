#sorting by function
def name_sorter(item):
    return item['name']

presenters = [
    {'name':'Susan', 'age':50},
    {'name':'Christopher', 'age':47}
]

#sort by name
presenters.sort(key=name_sorter)
print(presenters)

#-----------------------------
#Now Using lambda, without explicting declaring a single line function
#sort by name ascending
presenters.sort(key=lambda item: item['name'])
print(presenters)

#-----------------------------
#sort by length of name ascending
presenters.sort(key=lambda item: len(item['name']))
print(presenters)