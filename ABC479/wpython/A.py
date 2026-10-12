N = int(input())
i = 0
output = 0
for A in list(map(int,input().split())):
    i += 1
    if i % 2 == 0:
        continue
    output += A
print(output)