N, D = map(int,input().split())
T_list = list(map(int,input().split()))
double_click = False
for i in range(1,N):
    if T_list[i] - T_list[i-1] <= D:
        double_click = True
        break
print(T_list[i] if double_click else -1)