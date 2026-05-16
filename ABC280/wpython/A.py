H, W = map(int,input().split())
grid = [input() for _ in range(H)]
output = 0
for S in grid:
    for s in S:
        if s == "#":
            output += 1
print(output)