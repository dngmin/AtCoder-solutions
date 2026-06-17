N = int(input())
A_i_before = list()
for i in range(N):
    A_i = list()
    for j in range(i+1):
        if j == 0 or j == i:
            A_i.append(1)
        else:
            A_i.append(A_i_before[j-1] + A_i_before[j])
    A_i_before = A_i
    print(*A_i)