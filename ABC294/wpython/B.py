H, W = map(int,input().split())
grid = list(list(map(int,input().split())) for _ in range(H))
for i in range(H):
    for j in range(W):
        if grid[i][j] == 0:
            grid[i][j] = '.'
        else:
            grid[i][j] = chr(grid[i][j]+64)
for row in grid:
    print("".join(row))