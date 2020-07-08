board = [" " for i in range(9)]


def print_board():
    row1 = f"| {board[0]} | {board[1]} | {board[2]} |"
    row2 = f"| {board[3]} | {board[4]} | {board[5]} |"
    row3 = f"| {board[6]} | {board[7]} | {board[8]} |"

    print()
    print(row1)
    print(row2)
    print(row3)
    print()


def player_move(mark_type):
    player_number = 1
    if mark_type == "O":
        player_number = 2

    print(f"Your turn player {player_number}.")

    choice = int(input("Enter a board number (1-9): ").strip())
    if board[choice-1] == " ":
        board[choice-1] = mark_type
    else:
        print("\nThat space is taken !")


def is_win(mark_type):
    if (board[0] == mark_type and board[1] == mark_type and board[2] == mark_type) \
        or (board[3] == mark_type and board[4] == mark_type and board[5] == mark_type) \
        or (board[3] == mark_type and board[4] == mark_type and board[5] == mark_type) \
        or (board[0] == mark_type and board[3] == mark_type and board[6] == mark_type) \
        or (board[1] == mark_type and board[4] == mark_type and board[7] == mark_type) \
        or (board[2] == mark_type and board[5] == mark_type and board[8] == mark_type) \
        or (board[0] == mark_type and board[4] == mark_type and board[8] == mark_type) \
        or (board[2] == mark_type and board[4] == mark_type and board[6] == mark_type):
        return True
    else:
        return False


def is_draw():
    if " " not in board:
        return True
    else:
        return False

def game():
    print("***** Welcome to Tic Toe *****")
    print("player 1: X , player 2: O")
    print_board()

    while True:
        player_move("X")
        print_board()

        if is_win("X"):
            print("Player 1 Wins! Congratulations :)")
            break
        elif is_draw():
           print("It's a Draw!")
           break

        player_move("O")
        print_board()

        if is_win("O"):
            print("Player 2 Wins! Congratulations :)")
            break
       
        

if __name__ == "__main__":
    game()