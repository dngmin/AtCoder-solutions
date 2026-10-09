N, K = map(int,input().split())
output = 1
k = K
while N >= k:
    output += 1
    k *= K
print(output)