H, W, X, Y = map(int,input().split())
S = list(input() for _ in range(H))
X, Y = X-1, Y-1
output = 0
i = Y-1
while i >= 0:
    if S[X][i] == "#": break
    output += 1
    i -= 1
i = Y+1
while i < W:
    if S[X][i] == "#": break
    output += 1
    i += 1
i = X-1
while i >= 0:
    if S[i][Y] == "#": break
    output += 1
    i -= 1
i = X+1
while i < H:
    if S[i][Y] == "#": break
    output += 1
    i += 1

print(output + 1)