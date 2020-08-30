number_list = range(10)


# 1) normal way (imperative way) of doubling
doubled_list = []
for item in number_list:
    doubled_list.append(item * 2)

print(doubled_list)


# ------------------------------
# 2) using map (functional way)
def doubled(x):
    return x * 2


doubled_list_using_functional = list(map(doubled, number_list))
print(doubled_list_using_functional)
