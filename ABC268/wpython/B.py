S = input()
T = input()
if len(S) <= len(T):
    for i in range(len(S)):
        if S[i] != T[i]:
            print("No")
            break
    else:
        print("Yes")
else:
    print("No")