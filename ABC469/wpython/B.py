N = int(input())
S = input()
output = 0
for i in range(N):
    if S[i] == "x":
        if i == 0: L = False
        else: L = True if S[i-1] == "o" else False

        if i + 1 == N: R = False
        else: R = True if S[i+1] == "o" else False
    else: continue

    output += 0 if (L or R) else 1
print(output)