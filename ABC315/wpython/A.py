S = input()
tcdr = ("a","e","i","o","u")
for s in S:
    if s not in tcdr:
        print(s, end="")