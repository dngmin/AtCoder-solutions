N, K, A = map(int,input().split())
print(N if (A + K - 1) % N == 0 else (A + K - 1) % N)