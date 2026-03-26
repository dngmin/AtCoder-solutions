N = int(input())
WX_list = list()
for _ in range(N):
    W, X = map(int,input().split())
    WX_list.append([W,X])

output = 0
for plus_time in range(24):
    member = 0
    for W, X in WX_list:
        if 9 <= (X+plus_time)%24 <= 17:
            member += W
    if member > output:
        output = member
print(output)