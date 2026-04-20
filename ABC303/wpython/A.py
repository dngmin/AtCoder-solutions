N = int(input())
S = input()
T = input()
for i in range(N):
    if S[i] == T[i] or {S[i],T[i]} == {'o','0'} or {S[i],T[i]} == {'l','1'}:
        continue
    else:
        print("No")
        break
else:
    print("Yes")