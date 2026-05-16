N = int(input())
S_list = list(map(int,input().split()))
A_list = list()
sum_A = 0
for S in S_list:
    A = S - sum_A
    sum_A += A
    A_list.append(A)
print(*A_list)