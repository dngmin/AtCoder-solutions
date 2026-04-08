N, M = map(int,input().split())
player = list(range(1,N+1))

for _ in range(M):
    A, B = map(int,input().split())
    if B in player:
        player.remove(B)
print(player[0] if len(player) == 1 else -1)