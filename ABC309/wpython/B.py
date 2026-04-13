N = int(input())
grid = list(input() for _ in range(N))

print(grid[1][0] + grid[0][:-1])
for i in range(1,N-1):
    print(grid[i+1][0] + grid[i][1:-1] + grid[i-1][-1])
print(grid[N-1][1:] + grid[N-2][-1])