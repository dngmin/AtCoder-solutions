N, K = map(int,input().split())
A_list = list(map(int,input().split()))
for _ in range(K):
    A_list.pop(0)
    A_list.append(0)
print(*A_list)