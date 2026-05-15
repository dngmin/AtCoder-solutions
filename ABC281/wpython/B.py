S = input()
sandwich = False
if len(S) == 8:
    if ord("A") <= ord(S[0]) <= ord("Z"):
        if ord("A") <= ord(S[-1]) <= ord("Z"):
            for i in S[1:-1]:
                if not (ord("0") <= ord(i) <= ord("9")):
                    break
            else:
                if 100000 <= int(S[1:-1]) <= 999999:
                    sandwich = True
print("Yes" if sandwich else "No")