N = int(input())
ancestor = [0] * (N+1)
for i, P in enumerate(map(int,input().split()), start = 2):
    ancestor[i] = P
output = 0
while i != 1:
    i = ancestor[i]
    output += 1
print(output)