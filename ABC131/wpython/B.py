N, L = map(int,input().split())
apple_pie = L*N + (N)*(N+1)//2 - N
apple = 300
for i in range(1, N+1):
    if (L+i-1)**2 < apple**2:
        apple = L + i - 1
print(apple_pie - apple)