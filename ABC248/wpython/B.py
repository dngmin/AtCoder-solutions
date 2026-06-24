A, B, K = map(int,input().split())
output = 0
while not A >= B:
    A *= K
    output += 1
print(output)