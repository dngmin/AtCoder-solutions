N, P = map(int,input().split())
output = 0
for a in list(map(int,input().split())):
    if a < P: output += 1
print(output)