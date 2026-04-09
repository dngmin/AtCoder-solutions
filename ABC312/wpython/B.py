N, M = map(int,input().split())
grid = [input() for _ in range(N)]
LU_block = ["###.", "###.", "###.", "...."]
RD_block = ["....", ".###", ".###", ".###"]
for i in range(N-8):
    for j in range(M-8):
        if [grid[i][j:j+4], grid[i+1][j:j+4], grid[i+2][j:j+4], grid[i+3][j:j+4]] == LU_block:
            if [grid[i+5][j+5:j+9], grid[i+6][j+5:j+9], grid[i+7][j+5:j+9], grid[i+8][j+5:j+9]] == RD_block:
                print(i+1,j+1)