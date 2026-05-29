X, Y, Z = map(int,input().split())
if abs(X) < abs(Y) or X*Y < 0:
    print(abs(X))
else:
    if abs(Z) <= abs(Y):
        print(abs(X) if X*Z > 0 else abs(X)+abs(Z*2))
    else:
        print(-1)