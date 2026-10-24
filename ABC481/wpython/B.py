N, K = map(int,input().split())
output = 0
A_list = list(map(int,input().split()))
A_past = A_list[0]
output += A_past == K
for A in A_list[1:]:
    if A_past > K and A <= K:
        output += 1
    elif A_past < K and A >= K:
        output += 1
    A_past = A
print(output)