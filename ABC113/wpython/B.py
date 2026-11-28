N = int(input())
T, A = map(int,input().split())
H_list = list(map(int,input().split()))
best = -1
abs_minimum = 10**7
for i in range(N):
    diff = abs(A - (T - H_list[i] * 0.006))
    if diff < abs_minimum:
        best = i+1
        abs_minimum = diff
print(best)