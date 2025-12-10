def create_board(n):
    return [[0 for i in range(n)] for i in range(n)]


def visualize_board(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            symbol = "♛" if board[i][j] else "."
            print(" " + symbol, end="")
        print()
    print()

def make_is_safe():
    def is_safe(board, row, col):
        n = len(board)
        # check column
        for i in range(n):
            if board[i][col] == 1:
                return False
        for j in range(n):
            if board[row][j] == 1:
                return False
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row + 1, n), range(col - 1, -1, -1)):
            if i < n and board[i][j] == 1:
                return False
        return True
    return is_safe

def solve_col(board, col, is_safe):
    n = len(board)
    if col >= n:
        return True
    for row in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_col(board, col + 1, is_safe):
                return True
            board[row][col] = 0
    return False


def solve_n_queen(n, is_safe_func):
    board = create_board(n)
    if not solve_col(board, 0, is_safe_func):
        print(f"No solution exists for N = {n}")
        return
    visualize_board(board)

while True:
    print("1. Solve N-Queen")
    print("2. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        while True:
            n = int(input("Enter the value of N for N-Queen problem: "))
            if n <= 0:
                print("Please enter a positive integer N greater than 0.")
            else:
                break
        is_safe_func = make_is_safe()
        solve_n_queen(n, is_safe_func)
    elif ch == 2:
        break
    else:
        print("Please enter a valid choice.")
