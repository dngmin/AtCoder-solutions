N = int(input())
cards = [4] * (N+1)
for A in list(map(int,input().split())):
    cards[A] -= 1
for i in range(1,N+1):
    if cards[i]:
        print(i)
        break