N = int(input())
S_list = list()
for _ in range(N):
    S_list.append(input())
for i in range(N):
    print(S_list[N-i-1])