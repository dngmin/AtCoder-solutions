N = int(input())
A_grid = list(list(map(int,input().split())) for _ in range(N))
B_grid = list(list(map(int,input().split())) for _ in range(N))

matched = True
for i in range(N):
    for j in range(N):
        if A_grid[i][j] == 1 != B_grid[i][j]:
            matched = False
            break
    if not matched:
        break
if matched:
    print("Yes")
    exit()

matched = True
for i in range(N):
    for j in range(N):
        if A_grid[j][N-1-i] == 1 != B_grid[i][j]:
            matched = False
            break
    if not matched:
        break
if matched:
    print("Yes")
    exit()

matched = True
for i in range(N):
    for j in range(N):
        if A_grid[N-1-i][N-1-j] == 1 != B_grid[i][j]:
            matched = False
            break
    if not matched:
        break
if matched:
    print("Yes")
    exit()

matched = True
for i in range(N):
    for j in range(N):
        if A_grid[N-1-j][i] == 1 != B_grid[i][j]:
            matched = False
            break
    if not matched:
        break
print ("Yes" if matched else "No")