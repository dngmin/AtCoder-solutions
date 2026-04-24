N, T = map(int,input().split())
C_list = list(map(int,input().split()))
R_list = list(map(int,input().split()))
T_winner, T_rank = -1, -1
C_winner, C_rank = -1, -1

for i in range(N):
    C = C_list[i]
    R = R_list[i]
    if C == T:
        if R > T_rank:
            T_winner = i
            T_rank = R
    elif C == C_list[0]:
        if R > C_rank:
            C_winner = i
            C_rank = R
print(T_winner+1 if T_winner != -1 else C_winner+1)