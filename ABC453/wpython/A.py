N = int(input())
S = input()
o = True
for i in range(N):
    if S[i] != "o":
        break
print(S[i:] if S[i] != "o" else "")