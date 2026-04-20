N, M = map(int,input().split())
photo_group = [list(input().split()) for _ in range(M)]
not_bad = set()
for i in range(M):
    for j in range(N-1):
        not_bad.add("-".join(photo_group[i][j:j+2]))
        not_bad.add("-".join(photo_group[i][j:j+2][::-1]))
print((N*(N-1) - len(not_bad)) // 2)