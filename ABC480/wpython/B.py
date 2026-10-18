N, M = map(int,input().split())
Names = [input() for _ in range(N)]
voted = [0]*N
for _ in range(M):
    written = input()
    if written in Names:
        voted[Names.index(written)] += 1
    else:
        can_vote = list()
        for name in Names:
            if len(name) != len(written):
                continue
            mismatch = 0
            for j in range(len(name)):
                if name[j] != written[j]:
                    mismatch += 1
            if mismatch == 1:
                can_vote.append(name)
        if len(can_vote) == 1:
            voted[Names.index(can_vote[0])] += 1
for v in voted:
    print(v)