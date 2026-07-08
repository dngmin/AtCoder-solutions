S = input()
a, b = map(int,input().split())
for i in range(len(S)):
    if i+1 == a:
        print(S[b-1], end="")
    elif i+1 == b:
        print(S[a-1], end="")
    else: print(S[i], end="")