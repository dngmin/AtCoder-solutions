R, C = map(int,input().split())
grid = list(list(input()) for _ in range(R))
bombs = list()
for i in range(R):
    for j in range(C):
        if "#" != grid[i][j] != ".":
            bombs.append([i,j,int(grid[i][j])])
for i in range(R):
    for j in range(C):
        for bomb in bombs:
            if abs(bomb[0]-i) + abs(bomb[1]-j) <= bomb[2]:
                grid[i][j] = "."
                break
    print("".join(grid[i]))