# Input: A list / array with integers.  For example:
# [3, 4, 1, 2, 9]
# Returns:
#  Nothing. However, this function will print out
#  a pair of numbers that adds up to 10. For example,
#  1, 9.  If no such pair is found, it should print
#  "There is no pair that adds up to 10.".

def pair10(given_list):
    middle_point = len(given_list) // 2
    left_index = middle_point -1
    right_index = middle_point

    # sort them first and divide and conquer
    given_list.sort()

    pair = []

    while left_index >= 0 and right_index < len(given_list):
        print("left: ", given_list[left_index], " | right: ", given_list[right_index])

        if given_list[left_index] + given_list[right_index] < 10:
            right_index += 1
            continue
        elif given_list[left_index] + given_list[right_index] > 10:
            left_index -= 1
            continue
        
        pair.append([given_list[left_index], given_list[right_index]])

        left_index -= 1
        right_index += 1
        
    return pair if pair != [] else "There is no pair that adds up to 10."



if __name__ == "__main__":
    print("""
    Which pair adds up to 10? (Should print 1, 9)

    [3, 4, 1, 2, 9]
    """)

    result = pair10([3, 4, 1, 2, 9])
    print(result)


    print("""
    Which pair adds up to 10? (Should print -20, 30)

    [-11, -20, 2, 4, 30]
    """)

    result = pair10([-11, -20, 2, 4, 30])
    print(result)


    print("""
    Which pair adds up to 10? (Should print 1, 9 or 2, 8)

    [1, 2, 9, 8]
    """)

    result = pair10([1, 2, 9, 8])
    print(result)


    print("""
    Which pair adds up to 10? (Should print 1, 9)

    [1, 1, 1, 2, 3, 9]
    """)

    result = pair10([1, 1, 1, 2, 3, 9])
    print(result)


    print("""
    Which pair adds up to 10? (Should print "There is no pair that adds up to 10.")

    [1, 1, 1, 2, 3, 4, 5]
    """)

    result = pair10([1, 1, 1, 2, 3, 4, 5])
    print(result)