capital = False
small = False
letters = [False] * 58
for s in input():
    if 65 <= ord(s) <= 90:
        capital = True
    elif 97 <= ord(s) <= 122:
        small = True
    if not letters[ord(s) - 65]:
        letters[ord(s) - 65] = True
    else:
        print("No")
        break
else:
    print("Yes" if capital and small else "No")