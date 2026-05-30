grid = [input() for _ in range(10)]
in_square = False
B = None
for i in range(10):
    if grid[i] == "..........":
        if in_square:
            B = i
            break
        continue
    if not in_square:
        A = i
        in_square = True
    for C in range(10):
        if grid[i][C] == "#":
            break
    for D in range(9,-1,-1):
        if grid[i][D] == "#":
            break
print(A+1, B if B else 10)
print(C+1, D+1)