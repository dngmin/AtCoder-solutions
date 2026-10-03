N, M = map(int,input().split())
A_list = list(map(int,input().split()))
sum_A = sum(A_list)
popular = 0
for A in A_list:
    if 4 * A * M >= sum_A:
        popular += 1
print("Yes" if popular >= M else "No")