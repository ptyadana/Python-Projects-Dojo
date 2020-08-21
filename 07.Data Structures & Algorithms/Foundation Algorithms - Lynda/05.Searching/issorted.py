# determine if a list is sorted


items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def is_sorted_advance(itemList):
    return all(itemList[i] <= itemList[i+1] for i in range(len(itemList) - 1))


def is_sorted(itemlist):
    #  using the brute force method
    for i in range(len(itemlist)-1):
        if itemlist[i] > itemlist[i+1]:
            return False
    return True

print(is_sorted(items1))
print(is_sorted(items2))

print(is_sorted_advance(items1))
print(is_sorted_advance(items2))

