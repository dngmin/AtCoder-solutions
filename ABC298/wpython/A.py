N = int(input())
S = input()
good = None
bad = None
for s in S:
    if s == 'o':
        good = True
    elif s == 'x':
        bad = True
        break
print("Yes" if good and not bad else "No")