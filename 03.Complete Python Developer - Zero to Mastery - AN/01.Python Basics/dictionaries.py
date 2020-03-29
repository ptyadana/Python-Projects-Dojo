my_dict = {
    "a":"AAA",
    "b":"BBB",
    "c":"CCC"
}

print(my_dict["a"])

my_dict = {
    "a":"AAA",
    "b": [1,2,3,4],
    "c": True
}

print(my_dict["b"][1])

my_list =[
     {
    "a":"AAA",
    "b": [1,2,3,4],
    "c": True
},
{
    "a":"AAA",
    "b": [5,6,7,8],
    "c": True
}
]

print(my_list[1]['b'][2])