S = input()
i = 0
for s in S:
    i += S.count(s)
print("Yes" if i == 8 else "No")