N, M = map(int,input().split())
meet = [[False]*(N+1) for _ in range(N+1)]
for _ in range(M):
    k_x_list = list(map(int,input().split()))
    for x1 in k_x_list[1:]:
        for x2 in k_x_list[1:]:
            meet[x1][x2] = True
all_friends = True
for met in meet[1:]:
    if met.count(False) != 1:
        all_friends = False
        break
print("Yes" if all_friends else "No")