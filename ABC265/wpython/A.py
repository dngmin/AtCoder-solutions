X, Y, N = map(int,input().split())
if 3 * X <= Y:
    print(X * N)
else:
    if N % 3 == 0:
        print(N//3 * Y)
    else:
        print(N//3 * Y + N % 3 * X)