H, W = map(int,input().split())
grid = [input() for _ in range(H)]
p1 = False
for i in range(H):
    for j in range(W):
        if grid[i][j] == "o":
            if p1:
                print(abs(x - i) + abs(y - j))
                exit()
            else:
                p1 = True
                x, y = i, j