M, D = map(int,input().split())
S = list(input())
for i in range(M):
    if S[i] == "G":
        for j in range(max(0, i-D), min(i+D+1, M)):
            if S[j] == ".": S[j] = "#"
print(S.count("."))