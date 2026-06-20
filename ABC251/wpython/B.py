N, W = map(int,input().split())
A_list = list(map(int,input().split()))
good = [0] * (W+1)
for i in range(N):
    one = A_list[i]
    if one <= W:
        good[A_list[i]] += 1
    for j in range(i+1,N):
        two = A_list[i] + A_list[j]
        if two <= W:
            good[two] += 1
        for k in range(j+1,N):
            three = A_list[i] + A_list[j] + A_list[k]
            if three <= W:
                good[three] += 1
output = 0
for n in good:
    if n:
        output += 1
print(output)