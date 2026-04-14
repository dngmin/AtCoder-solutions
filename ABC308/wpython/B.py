N, M = map(int,input().split())
C_list = list(input().split())
D_list = list(input().split())
P_list = list(map(int,input().split()))
total = 0
for C in C_list:
    if C in D_list:
        total += P_list[D_list.index(C)+1]
    else:
        total += P_list[0]
print(total)