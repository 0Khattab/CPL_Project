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
