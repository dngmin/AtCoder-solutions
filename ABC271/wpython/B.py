N, Q = map(int,input().split())
L_list = [list(map(int,input().split())) for _ in range(N)]
for _ in range(Q):
    s, t = map(int,input().split())
    print(L_list[s-1][t])