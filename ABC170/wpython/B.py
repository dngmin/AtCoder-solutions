X, Y = map(int,input().split())
if Y % 2 != 0:
    print("No")
else:
    print("Yes" if 2*X <= Y <= 4*X else "No")