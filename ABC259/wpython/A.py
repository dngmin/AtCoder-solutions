N, M, X, T, D = map(int,input().split())
H = T - X*D
Y = 0
while Y != M:
    if Y < X:
        H += D
    Y += 1
print(H)