N = int(input())
candidate = {}
for _ in range(N):
    S = input()
    try:
        candidate[S] += 1
    except:
        candidate[S] = 1
maximum_voted = -1
who = None
for c in candidate:
    voted = candidate[c]
    if voted > maximum_voted:
        who = c
        maximum_voted = voted
print(who)