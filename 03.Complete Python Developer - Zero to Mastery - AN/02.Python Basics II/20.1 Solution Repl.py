#check duplicate in list
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']


#solution version 1, using sets
# my_set = set()
# duplicate_list = []

# for item in some_list:
#     if(item in my_set):
#         duplicate_list.append(item)
#     else:
#         my_set.add(item)

# print(f"duplicated item: {duplicate_list}")


#solution version 2, using lists
duplicate_list = []
unique_list = []

for item in some_list:
    if some_list.count(item) > 1:
        if item not in duplicate_list:
            duplicate_list.append(item)

print(f"duplicated items: {duplicate_list}")
