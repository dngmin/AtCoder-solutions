H, W = map(int,input().split())
A = list(input() for _ in range(H))
B = list(input() for _ in range(H))
for i in range(W):
    A_shift = list()
    for j in range(H):
        A_shift.append(A[j][i:]+A[j][:i])
    for k in range(H):
        if A_shift[k:] + A_shift[:k] == B:
            print("Yes")
            exit()
print("No")