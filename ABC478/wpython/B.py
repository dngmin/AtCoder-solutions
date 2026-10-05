N, V = map(int,input().split())
W_list = list(map(int,input().split()))
max_topping = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if i + j + k > V-3:
                continue
            max_topping = max(max_topping, W_list[i] + W_list[j] + W_list[k])
print(max_topping)