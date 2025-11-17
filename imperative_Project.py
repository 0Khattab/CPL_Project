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
    if n <= 0:
        print("Please enter a positive integer N greater than 0.")
        return
    
    board = create_board(n)

    if not solve_col(board, 0):
        print(f"No solution exists for N ={n}")
        return

    visualize_board(board)

n= int(input("Enter the value of N for N-Queen problem: "))
solve_n_queen(n)
