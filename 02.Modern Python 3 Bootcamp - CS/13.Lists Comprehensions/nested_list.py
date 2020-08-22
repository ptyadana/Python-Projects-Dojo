board = [[num for num in range(1,4)] for val in range(1,4)]
print(board)

results = [["X" if num%2 == 0 else "O" for num in range(3)] for i in range(3)]
print(results)