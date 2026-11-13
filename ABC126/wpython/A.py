N, K = map(int,input().split())
S = input()
for i in range(N):
    if i+1 == K:
        print(S[i].lower(),end="")
    else:
        print(S[i],end="")