N, M, T = map(int,input().split())
A_list = [0] + list(map(int,input().split()))
bonus = [0] * (N)
for _ in range(M):
    X, Y = map(int,input().split())
    bonus[X-1] = Y
for i in range(1, N):
    if T - A_list[i] <= 0:
        print("No")
        break
    T += -A_list[i] + bonus[i]
else:
    print("Yes")