S = input()
unreadable = True
odd = True
for s in S:
    if odd:
        if ord("a") <= ord(s) <= ord("z"):
            odd = False
        else: unreadable = False
    else:
        if ord("A") <= ord(s) <= ord("Z"):
            odd = True
        else: unreadable = False
    if not unreadable: break
print("Yes" if unreadable else "No")