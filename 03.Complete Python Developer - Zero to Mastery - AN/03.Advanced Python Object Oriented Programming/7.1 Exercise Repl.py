#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
kitty = Cat('kitty', 1)
catty = Cat('catty', 2)
fluffy = Cat ('fluffy', 3)

# cat_list = []
# cat_list.append(kitty)
# cat_list.append(catty)
# cat_list.append(fluffy)

# 2 Create a function that finds the oldest cat
# def find_oldest_cat(cat_list):
#     max_list = []
#     max_cat = Cat('dummy',0)
#     max_list.append(max_cat)

#     for cat in cat_list:
#         if cat.age > max_list[0].age:
#             max_list.pop()
#             max_list.append(cat)

#     return max_list[0]

def find_oldest_cat(*args):
    return max(args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
# print(f"The oldest cat is {find_oldest_cat(cat_list).age} years old.")

oldest_cat_age = find_oldest_cat(kitty.age, catty.age, fluffy.age)
print(f"The oldest cat is {oldest_cat_age} years old.")
