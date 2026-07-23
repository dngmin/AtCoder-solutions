S = input()
S_max = chr(96)
S_min = chr(123)
for i in range(len(S)):
    shifted = S[i:] + S[:i]
    if shifted >= S_max: S_max = shifted
    if shifted <= S_min: S_min = shifted
print(S_min)
print(S_max)