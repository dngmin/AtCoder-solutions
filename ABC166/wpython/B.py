N, K = map(int,input().split())
has_candy = [False] * (N+1)
for _ in range(K):
    d = int(input())
    for A in list(map(int,input().split())):
        has_candy[A] = True
print(has_candy[1:].count(False))