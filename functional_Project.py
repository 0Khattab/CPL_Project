def is_safe(row, col, columns, diag1, diag2):
    return col not in columns and (row - col) not in diag1 and (row + col) not in diag2
