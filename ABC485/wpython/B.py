N, M = map(int,input().split())
Faucets = list(input() for _ in range(N))
for n in range(N):
    if Faucets[n] == "x"*M:
        print("Faucet",n+1)
        break
for m in range(M):
    d = ""
    for n in range(N):
        d += Faucets[n][m]
    if d == "x"*N:
        print("Drain", m+1)
        break