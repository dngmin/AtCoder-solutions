S = input()
B1, B2 = None, None
R1, R2 = None, None
K = None
for i in range(len(S)):
    if S[i] == "B":
        if B1 is None:
            B1 = i
        else:
            B2 = i
    elif S[i] == "R":
        if R1 is  None:
            R1 = i
        else:
            R2 = i
    elif S[i] == "K":
        K = i
if (B1%2 != B2%2) and R1 < K < R2:
    print("Yes")
else:
    print("No")