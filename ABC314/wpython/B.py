N = int(input())
players = [[int(input()), list(map(int,input().split()))] for _ in range(N)]
X = int(input())
winners = list()
win_count = 37

for player, [bet_count, bet] in enumerate(players):
    if X in bet:
        if bet_count < win_count:
            winners = [player+1]
            win_count = bet_count
        elif bet_count == win_count:
            winners.append(player+1)
print(len(winners))
print(" ".join(map(str,winners)))