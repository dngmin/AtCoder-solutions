bingo_set = [list(map(int,input().split()))
            ,list(map(int,input().split()))
            ,list(map(int,input().split()))]
for _ in range(int(input())):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if bingo_set[i][j] == b:
                bingo_set[i][j] = 0
                b = False
            if not b: break
        if not b: break

if sum([bingo_set[0][0], bingo_set[1][1], bingo_set[2][2]]) == 0:
    print("Yes")
elif sum([bingo_set[0][2], bingo_set[1][1], bingo_set[2][0]]) == 0:
    print("Yes")
else:
    for i in range(3):
        if sum(bingo_set[i]) * sum([bingo_set[0][i], bingo_set[1][i], bingo_set[2][i]]) == 0:
            print("Yes")
            break
    else:
        print("No")