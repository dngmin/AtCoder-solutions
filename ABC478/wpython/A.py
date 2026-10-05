N, M = map(int,input().split())
people = [M//N] * N
for i in range(M % N):
    people[i] += 1
for p in people:
    print(p)