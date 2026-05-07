N, K = map(int,input().split())
S_list = list()
i = 0
for _ in range(N):
    S = input()
    if i < K:
        S_list.append(S)
        i += 1
S_list.sort()
for S in S_list:
    print(S)