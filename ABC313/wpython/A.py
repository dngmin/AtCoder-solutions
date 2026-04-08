N = int(input())
P_list = list(map(int,input().split()))
if len(P_list) == 1:
    print(0)
else:
    max_P = max(P_list[1:])
    print(0 if max_P < P_list[0] else max_P - P_list[0] + 1)