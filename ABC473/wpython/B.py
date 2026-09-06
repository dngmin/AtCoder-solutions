N = int(input())
deck = [0] * 101
for A in list(map(int,input().split())):
    if deck[A] == A: deck[A] = 0
    else: deck[A] = A
print(sum(deck))