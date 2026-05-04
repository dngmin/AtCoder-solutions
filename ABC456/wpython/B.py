Dice1 = list(map(int,input().split()))
Dice2 = list(map(int,input().split()))
Dice3 = list(map(int,input().split()))
count = 0
for A1 in Dice1:
    for A2 in Dice2:
        for A3 in Dice3:
            count += 1 if A1*A2*A3 == 120 else 0
print(count/(6*6*6))