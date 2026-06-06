cards = [0]*14
for i in map(int,input().split()):
    cards[i] += 1
print("Yes" if sorted(set(cards)) == [0, 2, 3] else "No")