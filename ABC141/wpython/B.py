Odd = True
for s in input():
    if Odd:
        if not (s in ["R", "U", "D"]):
            print("No")
            break
    else:
        if not (s in ["L", "U", "D"]):
            print("No")
            break
    Odd = not Odd
else:
    print("Yes")