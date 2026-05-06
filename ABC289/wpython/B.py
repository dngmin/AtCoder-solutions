N ,M = map(int,input().split())
a_list = list(map(int,input().split()))
G = [0] * (N+1)
for a in a_list:
    G[a] = 1
start = False
for i in range(1,N):
    if G[i] == 1:
        if start: continue
        else: start = i

    else:
        if start:
            print(" ".join(map(str,range(i,start-1,-1))), end=" ")
            start = False
        else:
            print(i, end=" ")
if start:
    print(" ".join(map(str,range(N,start-1,-1))))
else:
    print(N)