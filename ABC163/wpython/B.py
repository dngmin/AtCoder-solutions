N, M = map(int,input().split())
A_sum = sum(list(map(int,input().split())))
print(N - A_sum if N >= A_sum else -1)