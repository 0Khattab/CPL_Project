def is_safe(board, row, col, n):
    for i in range(n):
        if board[i][col] == 1:
            return False
    
    for j in range(n):
        if board[row][j] == 1:
            return False
    
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row+1, n), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    return True
    
def solve_col(board, col):
    n = len(board)

    if col >= n:
        return True

    for row in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve_col(board, col + 1):
                return True

            board[row][col] = 0

    return False


def solve_n_queen(n):
    board = create_board(n)

    if not solve_col(board, 0):
        print(f"No solution exists for N ={n}")
        return

    visualize_board(board)

while True:
    n = int(input("Enter the value of N for N-Queen problem: "))
    if n <= 0:
        print("Please enter a positive integer N greater than 0.")
    
    if n > 0:
        break

solve_n_queen(n)
