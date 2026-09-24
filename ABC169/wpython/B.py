N = int(input())
output = 1
over = False
for A in list(map(int,input().split())):
    if A == 0:
        print(0)
        break
    if over:
        continue
    output *= A
    if output > 10**18: over = True
else:
    print(-1 if over else output)