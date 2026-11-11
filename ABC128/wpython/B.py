N = int(input())
Guidebook = dict()
index = dict()
for i in range(N):
    S, P = input().split()
    index[S+P] = i+1
    P = int(P)
    try:
        Guidebook[S].append(P)
    except:
        Guidebook[S] = [P]
for city in sorted(Guidebook):
    for p in sorted(Guidebook[city], reverse= True):
        print(index[city+str(p)])