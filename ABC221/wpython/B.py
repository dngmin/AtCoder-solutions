S = input()
T = input()
for i in range(len(S)-1):
    if T == S[:i] + S[i+1] + S[i] + S[i+2:]:
        print("Yes")
        break
else:
    print("Yes" if S == T else "No")