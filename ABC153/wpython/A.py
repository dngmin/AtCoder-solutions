H, A = map(int,input().split())
print(H // A + (0 if H % A == 0 else 1))