N, M = map(int,input().split())
links = [set() for _ in range(N+1)]
output = 0
for _ in range(M):
    U, V = map(int,input().split())
    links[U].add(V)
    links[V].add(U)
for i in range(1,N-1):
    for j in range(i+1, N):
        for k in range(j+1, N+1):
            if {j,k} <= links[i] and {i,k} <= links[j] and {i,j} <= links[k]:
                output += 1
print(output)