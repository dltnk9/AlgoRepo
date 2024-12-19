a, b = map(int, input().split())
board = [input() for _ in range(a)]

def count_repaints(board, start_row, start_col, first_color):
    repaints = 0
    for i in range(8):
        for j in range(8):
            expected_color = first_color if (i + j) % 2 == 0 else ('B' if first_color == 'W' else 'W')
            if board[start_row + i][start_col + j] != expected_color:
                repaints += 1
    return repaints

min_repaints = float('inf')

for i in range(a - 7):
    for j in range(b - 7):
        repaints_w = count_repaints(board, i, j, 'W')
        repaints_b = count_repaints(board, i, j, 'B')
        min_repaints = min(min_repaints, repaints_w, repaints_b)

print(min_repaints)