H, W = map(int,input().split())
A_grid = list(list(input().split()) for _ in range(H))
for i in range(W):
    for j in range(H):
        print(A_grid[j][i], end = " ")
    print("")