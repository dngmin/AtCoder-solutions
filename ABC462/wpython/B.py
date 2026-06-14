N = int(input())
received = [[0] for _ in range(N+1)]
for i in range(N):
    sent = list(map(int,input().split()))
    for s in sent[1:]:
        received[s][0] += 1
        received[s].append(i+1)
for r in received[1:]:
    print(r[0]," ".join(map(str,sorted(set(r[1:])))))