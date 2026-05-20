shapes = ["H", "D", "C", "S"]
numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
N = int(input())
cards = list()
validation = True
for _ in range(N):
    card = input()
    s, n = card[0], card[1]
    if s in shapes and n in numbers and not card in cards:
        cards.append(card)
    else:
        validation = False
print("Yes" if validation else "No")