H, W = map(int,input().split())
grid = [input() for _ in range(H)]
dir = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]

for i in range(H):
    for j in range(W):
        if grid[i][j] == "s":
            for y, x in dir:
                snuke = ""
                if 0 <= i+y*4 < H and 0 <= j+x*4 < W:
                    for k in range(5):
                        snuke += (grid[i+y*k][j+x*k])
                    if snuke == "snuke":
                        for l in range(5):
                            print(i+y*l+1, j+x*l+1)
                        exit()