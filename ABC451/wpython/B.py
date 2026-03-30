N, M = map(int,input().split())
this_term = [0] * (M + 1)
next_term = [0] * (M + 1)
for _ in range(N):
    A, B = map(int,input().split())
    this_term[A] += 1
    next_term[B] += 1
for i in range(1,M+1):
    print(next_term[i] - this_term[i])