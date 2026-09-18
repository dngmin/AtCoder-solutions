N, D = map(int,input().split())
output = 0
for _ in range(N):
    X, Y = map(int,input().split())
    output += X*X + Y*Y <=D*D
print(output)