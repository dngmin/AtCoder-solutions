N, K = map(int,input().split())
output = 0
output += N * (N+1) // 2 * K * 100
output += K * (K+1) // 2 * N
print(output)