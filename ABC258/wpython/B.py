N = int(input())
grid = [input() for _ in range(N)]
bigest_start = 0
bigest = 0
for i in range(N):
    for j in range(N):
        if int(grid[i][j]) >= bigest_start:
            bigest_start = int(grid[i][j])
            u, ur, r, dr, d, dl, l, ul = 0, 0, 0, 0, 0, 0, 0, 0,
            for k in range(N):
                u += int(grid[(i - k) % N][j]) * 10**(N-k-1)
                ur += int(grid[(i - k) % N][(j + k) % N]) * 10**(N-k-1)
                r += int(grid[i][(j + k) % N]) * 10**(N-k-1)
                dr += int(grid[(i + k) % N][(j + k) % N]) * 10**(N-k-1)
                dl += int(grid[(i + k) % N][(j - k) % N]) * 10**(N-k-1)
                l += int(grid[i][(j - k) % N]) * 10**(N-k-1)
                ul += int(grid[(i - k) % N][(j - k) % N]) * 10**(N-k-1)
            bigest = max(bigest, u, ur, r, dr, d, dl, l, ul)

print(bigest)