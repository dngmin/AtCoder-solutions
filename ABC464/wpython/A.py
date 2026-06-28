S = input()
E = 0
W = 0
for s in S:
    if s == 'E': E += 1
    else: W += 1
print("East" if E > W else "West")