N = int(input())
grid = [input() for _ in range(N)]
correct = True
for i in range(N):
    for j in range(i+1,N):
        merge = grid[i][j] + grid[j][i]
        if not merge in ["WL", "LW", "DD"]:
            print("incorrect")
            exit()
print("correct")