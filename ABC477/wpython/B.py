N, D = map(int,input().split())
X_list = list(map(int,input().split()))
apart = list()
for i in range(N):
    for j in range(N):
        if i == j: continue

        if D > (X_list[i] - X_list[j]) > -D:
            break
    else:
        apart.append(i+1)
print(len(apart))
print(*apart)