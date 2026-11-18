S = input()
longest = 0
ACGT = "ACGT"
for i in range(len(S)):
    length = 0
    for j in range(i,len(S)):
        if S[j] in ACGT:
            length += 1
        else:
            break
    longest = max(longest, length)
print(longest)