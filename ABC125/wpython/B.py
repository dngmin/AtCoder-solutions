N = int(input())
V_list = list(map(int,input().split()))
C_list = list(map(int,input().split()))
output = 0
for i in range(N):
    margin = V_list[i] - C_list[i]
    if margin > 0:
        output += margin
print(output)