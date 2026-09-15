S = input()
T = input()
len_T = len(T)
minimum = 1000
for i in range(len(S) - len_T + 1):
    change = 0
    for j in range(len_T):
        if S[i+j] != T[j]: change += 1
    minimum = min(minimum, change)
print(minimum)