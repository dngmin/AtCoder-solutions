N, M = map(int,input().split())
output = 0
while (not M == 0):
    M = N % M
    output += 1
print(output)