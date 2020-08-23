# Problem: Counting the number of negative numbers.
# You are given a 2-dimensional array with integers.

# Example Input:
# [[-4, -3, -1, 1],
#  [-2, -2, 1, 2],
#  [-1,  1,  2, 3],
#  [ 1,  2,  4, 5]]

# Write a function, count_negatives(input), which finds and returns the number of negative integers in th array.


# Input: A 2-dimensional array with integers.  Example below.
#[[-4, -3, -1, 1],
# [-2, -2,  1, 2],
# [-1,  1,  2, 3],
# [ 1,  2,  4, 5]]
# Returns:
#  The number of negative numbers in the array.
#  In the above case, this function should return 6
#  since there are 6 negative numbers in the array.

def count_negatives(given_array):
    n = len(given_array)
    count = 0

    for i in range(n):
        for j in range(n):
            if given_array[i][j] < 0:
                count += 1
    return count

    


if __name__ == "__main__":

    print("""
    How many negative numbers are there in the following array?
    (There are 6.)

    [[-4, -3, -1, 1],
    [-2, -2,  1, 2],
    [-1,  1,  2, 3],
    [ 1,  2,  4, 5]]
    """)

    result = count_negatives(
    [[-4, -3, -1, 1],
    [-2, -2,  1, 2],
    [-1,  1,  2, 3],
    [ 1,  2,  4, 5]])

    print(result)


    print("""
    How many negative numbers are there in the following array?
    (There is 1.)

    [[-1, 0],
    [0,  0]]
    """)

    result = count_negatives(
    [[-1, 0],
    [0,  0]])

    print(result)


    print("""
    How many negative numbers are there in the following array?
    (There are 2.)

    [[-2, 0],
    [-1, 0]]
    """)

    result = count_negatives(
    [[-2, 0],
    [-1, 0]])
    print(result)

    print("""
    How many negative numbers are there in the following array?
    (There are none.)

    [[0]]
    """)

    result = count_negatives([[0]])
    print(result)