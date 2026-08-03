S, T = map(int,input().split())
a, b, c = 1, 1, 1
output = 0
for a in range(S+1):
    for b in range(S+1):
        for c in range(S+1):
            if a+b+c <= S and a*b*c <= T:
                output += 1
print(output)