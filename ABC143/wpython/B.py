N = int(input())
d_list = list(map(int,input().split()))
output = 0
for i in range(N):
    for j in range(N):
        if i == j: continue
        output += d_list[i] * d_list[j]
print(output // 2)