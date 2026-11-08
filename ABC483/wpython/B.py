N, Q = map(int,input().split())
deck = list(range(1,N+1))
for k in list(map(int,input().split())):
    deck = [-1 * c for c in deck[:k:][::-1]] + deck[k:]
for c in deck:
    print(c)