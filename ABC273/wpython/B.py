X, K = map(int,input().split())
for i in range(K):
    X //= 10**i
    if X%10 >= 5: X += (10 - X%10)
    else: X -= X%10
    X *= 10**i
print(X)