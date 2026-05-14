N, M = map(int,input().split())
S_list = list(int(input().replace('o','1').replace('x','0'),2) for _ in range(N))
output = 0
for i in range(N-1):
    for j in range(i+1,N):
        output += 1 if S_list[i] | S_list[j] == 2**M -1 else 0
print(output)