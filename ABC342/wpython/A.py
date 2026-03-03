S = input()
S_set = set()
for s in S:
    S_set.add(s)
    if len(S_set) == 2:
        break
for s in S_set:
    if S.count(s) == 1:
        print(S.index(s)+1)
        break