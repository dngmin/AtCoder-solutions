N = int(input())
W_list = list(map(int,input().split()))
minimum = 10e9
for i in range(1,N):
    diff = sum(W_list[:i]) - sum(W_list[i:])
    if diff**2 < minimum**2:
        minimum = diff if diff > 0 else -diff
print(minimum)