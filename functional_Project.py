def is_safe(row, col, columns, diag1, diag2):
    return col not in columns and (row - col) not in diag1 and (row + col) not in diag2

def create_board(n):
    return [["." for _ in range(n)] for _ in range(n)]

def visualize_board(board):
    return "\n".join([" ".join(row) for row in board])