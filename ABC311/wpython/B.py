N, D = map(int,input().split())
S_list = [int(input().replace("x","0").replace("o","1"), 2)for _ in range(N)]
target = 2**D - 1
for S in S_list:
    target &= S
vacations = bin(target)[2:].split("0")
print(max(len(vacation) for vacation in vacations))