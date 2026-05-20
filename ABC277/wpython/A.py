N, X = map(int,input().split())
P_list = list(map(int,input().split()))
for i in range(N):
    if X == P_list[i]:
        print(i+1)
        break