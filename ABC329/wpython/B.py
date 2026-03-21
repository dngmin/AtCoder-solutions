N = int(input())
A_list = list(map(int,input().split()))
A_max = max(A_list)
output = 0
for A in A_list:
    if A > output and A != A_max:
        output = A
print(output)