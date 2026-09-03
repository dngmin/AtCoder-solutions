H, W = map(int,input().split())
block = 0
m = -1
count = 0
for i in range(H):
    row = list(map(int,input().split()))
    for j in range(W):
        if m == -1:
            m = row[j]
            count += 1
            continue
        if row[j] >= m:
            block += row[j] - m
        elif row[j] < m:
            block += (m - row[j]) * count
            m = row[j]
        count += 1
print(block)