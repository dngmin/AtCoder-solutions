H, W = map(int,input().split())
grid = list(input() for _ in range(H))
output = [0] * W
for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            output[j] += 1
print(*output)