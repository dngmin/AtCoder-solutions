N, D = map(int,input().split())
coordinates = list(list(map(int,input().split())) for _ in range(N))
count = 0
for i in range(N-1):
    for j in range(i+1,N):
        distance2 = 0
        for k in range(D):
            distance2 += (coordinates[i][k] - coordinates[j][k]) ** 2
        count += (distance2**0.5) % 1 == 0
print(count)