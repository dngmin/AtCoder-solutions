cycle = [False] * 4
for _ in range(4):
    S = input()
    if S == "H": cycle[0] = True
    elif S == "2B": cycle[1] = True
    elif S == "3B": cycle[2] = True
    elif S == "HR": cycle[3] = True
print("No" if False in cycle else "Yes")