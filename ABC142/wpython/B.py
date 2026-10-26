N, K = map(int,input().split())
output = 0
for h in list(map(int,input().split())):
    output += h >= K
print(output)