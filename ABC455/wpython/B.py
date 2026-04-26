H, W = map(int,input().split())
S_grid = list(input() for _ in range(H))
output = 0
for h1 in range(H):
    for h2 in range(h1,H):
        for w1 in range(W):
            for w2 in range(w1, W):
                symm = True
                for i in range(h1,h2+1):
                    for j in range(w1,w2+1):
                        if S_grid[i][j] != S_grid[h1+h2-i][w1+w2-j]:
                            symm = False
                            break
                    if not symm:
                        break
                if symm:
                    output += 1
print(output)