N, X = map(int,input().split())
for s in input():
    if s == "o": X+=1
    else:
        X = max(0, X-1)
print(X)