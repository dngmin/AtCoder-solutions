N, M, C = map(int,input().split())
B_list = list(map(int,input().split()))
count = 0
for _ in range(N):
    A_list = list(map(int,input().split()))
    correct = C
    for i in range(M):
        correct += A_list[i] * B_list[i]
    count += correct > 0
print(count)