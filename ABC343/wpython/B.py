N = int(input())
A_grid = [list(input().split()) for _ in range(N)]
for row_A in A_grid:
    output = []
    for i in range(N):
        if row_A[i] == "1":
            output.append(str(i+1))
    print(" ".join(output))