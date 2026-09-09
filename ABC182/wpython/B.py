N = int(input())
A_list = list(map(int,input().split()))
max_GCD = -1
max_k = -1
for k in range(2,max(A_list)+1):
    GCD = 0
    for A in A_list:
        GCD += 1 if A % k == 0 else 0
    if GCD > max_GCD:
        max_GCD = GCD
        max_k = k
print(max_k)