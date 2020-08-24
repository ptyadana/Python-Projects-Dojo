def get_list_length(my_list):
    if my_list == []:
        return 0
    else:
        return 1 + get_list_length(my_list[1:])
    
if __name__ == "__main__":
    lst = list(range(10))
    print(get_list_length(lst))