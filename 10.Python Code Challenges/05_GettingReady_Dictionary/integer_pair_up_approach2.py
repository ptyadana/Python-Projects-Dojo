# Input: A list / array with integers.  For example:
# [3, 4, 1, 2, 9]
# Returns:
#  Nothing. However, this function will print out
#  a pair of numbers that adds up to 10. For example,
#  1, 9.  If no such pair is found, it should print
#  "There is no pair that adds up to 10.".

def pair10(given_list):
    numbers_seen = {}
    for item in given_list:
        if (10 - item) in numbers_seen:
            return [(10-item), item]
        else:
            numbers_seen[item] = 1


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