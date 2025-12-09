
# --------------- create and change board ---------------- #
def create_row(n, i=0):
    if i == n:
        return ()
    return (0,) + create_row(n, i + 1)

def create_board(n, i=0):
    if i == n:
        return ()
    return (create_row(n),) + create_board(n, i + 1)

def set_queen(board, row, col, r=0):
    if r == len(board):
        return ()
    current_row = board[r]
    if r == row:
        new_row = set_value_in_row(current_row, col)
        return (new_row,) + set_queen(board, row, col, r + 1)
    else:
        return (current_row,) + set_queen(board, row, col, r + 1)

def set_value_in_row(row, col, c=0):
    if c == len(row):
        return ()
    if c == col:
        return (1,) + set_value_in_row(row, col, c + 1)
    return (row[c],) + set_value_in_row(row, col, c + 1)

# ------------------------------------------------- #

# --------------- Safty for set queen ---------------- #
def check_left_row(board, row, col):
    if col < 0:
        return True
    if board[row][col] == 1:
        return False
    return check_left_row(board, row, col - 1)

def check_upper_left(board, row, col):
    if row < 0 or col < 0:
        return True
    if board[row][col] == 1:
        return False
    return check_upper_left(board, row - 1, col - 1)

def check_lower_left(board, row, col, n):
    if row >= n or col < 0:
        return True
    if board[row][col] == 1:
        return False
    return check_lower_left(board, row + 1, col - 1, n)

def is_safe(board, row, col):
    n = len(board)
    return (
        check_left_row(board, row, col - 1) and
        check_upper_left(board, row - 1, col - 1) and
        check_lower_left(board, row + 1, col - 1, n)
    )
# ----------------------------------------------------- #

# --------------- solve N-Queen ---------------- #
def try_row(board, col, row, n):
    if row == n:
        return False, board

    if is_safe(board, row, col):
        new_board = set_queen(board, row, col)
        success, result_board = solve_column(new_board, col + 1, n)

        if success:
            return True, result_board

        return try_row(board, col, row + 1, n)

    return try_row(board, col, row + 1, n)


def solve_column(board, col, n):
    if col == n:
        return True, board
    return try_row(board, col, 0, n)


def solve_nqueen(n):
    board = create_board(n)
    success, final_board = solve_column(board, 0, n)
    return success, final_board
# --------------------------------------------------- #

# --------------- Visuallization ---------------- #
def print_row(row, c=0):
    if c == len(row):
        return ""
    symbol = "♛" if row[c] else "."
    rest = print_row(row, c + 1)
    return symbol + (" " + rest if rest else "")


def print_board(board, r=0):
    if r == len(board):
        return
    print(print_row(board[r]))
    print_board(board, r + 1)
# ----------------------------------------------------- #
def Prog ():
    n = int(input("Please Enter Number of Queens: "))
    if n <= 0:
        print("Please enter a positive integer")
        Prog()
    else:
        success, board = solve_nqueen(n)
        if success:
            print_board(board)
            print("\n//////////////////\n")
        else:
            print("No solution.")
            print("\n//////////////////\n")
        return

def Main ():
    print("1. Solve n-queen")
    print("2. Exit")
    ch = int(input("Please enter your choice: "))
    if ch == 1:
        Prog()
        Main()
    elif ch == 2:
        return
    else:
        print("Please enter a valid choice.")
        print("\n//////////////////\n")
# ----------------------------------------------------- #

        
#------------Main fun-----------------#
Main()
