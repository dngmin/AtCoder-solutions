N = int(input())
m = -1
for _ in range(N):
    A, P, X = map(int,input().split())
    if A < X:
        if m == -1: m = P
        else: m = min(m,P)
print(m)