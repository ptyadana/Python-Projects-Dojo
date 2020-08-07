def bubble_sort(items, ascending = True):
    n = len(items)
    is_sorted = True
    
    for i in range(n):
        for j in range(1, n - i):
            if ascending:
                if items[j] < items[j-1]:
                    items[j], items[j-1] = items[j-1], items[j]
                    is_sorted = False
            else:
                if items[j] > items[j-1]:
                    items[j], items[j-1] = items[j-1], items[j]
                    is_sorted = False
        # immediate return for already sorted ones
        if is_sorted:
            return items

    return items

if __name__ == "__main__":
    items = [8, 2, 4, 1, 3]
    # items = [8, 2, 4]
    # items = [8, 2]
    # items = [8]
    # items = []
    # items = [1, 2, 3, 4, 8]

    print("items: ", items)

    sorted_one = bubble_sort(items)
    print("After ascending, sorted items: ", sorted_one)

    sorted_one = bubble_sort(items, ascending = False)
    print("After decending, sorted items: ", sorted_one)