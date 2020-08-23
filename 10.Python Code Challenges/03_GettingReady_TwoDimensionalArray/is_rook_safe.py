# Input:
#  chessboard: A 2-dimensional array that represents.  Example below.
#  [[1, 0, 0, 0],
#  [0, 1, 0, 0],
#  [0, 0, 0, 1],
#  [0, 0, 0, 0]]
# Returns:
#  True if none of the rooks can attack each other.
#  False if there is at least one pair of rooks that can attack each other.

def rooks_are_safe(chessboard):
    tracker = {}

    n = len(chessboard)
    for i in range(n):
        for j in range(n):
            
            row_count = tracker.get(f"row{i}", 0)
            col_count = tracker.get(f"col{j}", 0)

            if chessboard[i][j] == 1:
                row_count += 1
                col_count += 1

            # print("i:", i, ", j:", j, "|| row_count: ", row_count, ", col_count: ", col_count)
            # print(tracker)

            tracker[f"row{i}"] = row_count
            tracker[f"col{j}"] = col_count

            if row_count > 1 or col_count > 1:
                return False

    return True



if __name__ == "__main__":

    print("""
    Are rooks safe in this board? (Should be True.)
    [[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]]
    """)

    result = rooks_are_safe(
    [[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]])

    print(result)

    print("""
    Are rooks safe in this board? (Should be False.)
    [[1, 0],
    [1, 0]]
    """)

    result = rooks_are_safe(
    [[1, 0],
    [1, 0]])

    print(result)


    print("""
    Are rooks safe in this board? (Should be True.)
    [[1]]
    """)

    result = rooks_are_safe([[1]])
    print(result)

    print("""
    Are rooks safe in this board? (Should be False.)
    [[0, 0, 0],
    [1, 0, 1],
    [0, 0, 0]]
    """)

    result = rooks_are_safe(
    [[0, 0, 0],
    [1, 0, 1],
    [0, 0, 0]])

    print(result)