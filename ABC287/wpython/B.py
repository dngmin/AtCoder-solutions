N, M = map(int,input().split())
S_list = list()
for _ in range(N):
    S_list.append(int(input())%1000)
T_set = set()
for _ in range(M):
        T_set.add(int(input()))
for S in S_list:
      N -= 0 if S in T_set else 1
print(N)