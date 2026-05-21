N, M = map(int,input().split())
info = [set() for _ in range(N+1)]
for _ in range(M):
    A, B = map(int,input().split())
    info[A].add(B)
    info[B].add(A)

for i in range(1,N+1):
    info_list = list(info[i])
    info_list.sort()
    print(len(info_list),*info_list)