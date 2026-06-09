L1, R1, L2, R2 = map(int,input().split())
line1 = set(range(L1,R1+1))
line2 = set(range(L2,R2+1))
intersection = line1 & line2
print(len(intersection) -1 if intersection else 0)