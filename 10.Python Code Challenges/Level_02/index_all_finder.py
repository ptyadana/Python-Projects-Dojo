# Challenge: to index all items of a search term, in a list

"""
Input: list to search, value to search for
Output: list of indices
Note: list can contain lists too ie:multi-diemensions
Example: [[[1,2,3], 2, [1,3]], [1,2,3]]   => search for 2 => [[0,0,1], [0, 1], [1,1] ]
"""

def index_all_finder(items, search_value):
    index_lst = []
    for i in range(len(items)):
        if search_value == items[i]:
            index_lst.append([i])
        elif isinstance(items[i], list):
            for index in index_all_finder(items[i], search_value):
                index_lst.append([i]+index)
    return index_lst
    

if __name__ == "__main__":
    my_list = [[[1,2,3], 2, [1,3]], [1,2,3]]
    value_to_search = 2
    results = index_all_finder(my_list, value_to_search)
    print(results)