N, K, Q = map(int,input().split())
board = [0] * (N+1)
for i, A in enumerate(list(map(int,input().split())), start = 1):
    board[A] = i
for L in list(map(int,input().split())):
    i = 0
    count = 0
    for p in board:
        if p != 0:
            count += 1
            if count == L:
                break
        i += 1
    if i != N:
        if board[i+1] == 0:
            board[i+1] = p
            board[i] = 0
for i, p in enumerate(board):
    if p != 0:
        print(i, end= " ")