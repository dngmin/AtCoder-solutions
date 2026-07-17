S, T, X = map(int,input().split())
if T > S:
    print("Yes" if T > X + 0.5 >= S else "No")
else:
    print("Yes" if T > X or X >= S else "No" )