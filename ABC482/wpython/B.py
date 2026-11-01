bingo_board = list(input() for _ in range(5))
minimum = 5
for i in range(5):
    vertical = 0
    for j in range(5):
        vertical += bingo_board[j][i] == '.'
    minimum = min(minimum, bingo_board[i].count('.'),vertical)
diagonal_l = 0
diagonal_r = 0
for i in range(5):
    diagonal_l += bingo_board[i][i] == '.'
    diagonal_r += bingo_board[i][4-i] == '.'
print(min(minimum, diagonal_l, diagonal_r))