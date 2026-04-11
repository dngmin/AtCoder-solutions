N, M = map(int,input().split())
products = [list(map(int,input().split())) for _ in range(N)]
yes = False
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if products[i][0] >= products[j][0]:
            merge = set(products[i][2:])|set(products[j][2:])
            if len(merge) == products[j][1]:
                if products[i][0] > products[j][0] or products[i][1] < products[j][1]:
                    yes = True
        if yes:
            break
    if yes:
        break
print("Yes" if yes else "No")