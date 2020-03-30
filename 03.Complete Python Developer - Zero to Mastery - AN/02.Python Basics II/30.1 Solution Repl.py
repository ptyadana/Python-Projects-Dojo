def highest_even(li):
    max = 0
    for item in li:
        if item%2 == 0 and item > max:
            max = item
    return max

#version 2
def highest_even2(li):
    even_list = []
    for item in li:
        if item%2 == 0:
            even_list.append(item)
    return max(even_list)


print(highest_even([10,2,3,4,8,11]))
print(highest_even2([10,2,3,4,8,11]))