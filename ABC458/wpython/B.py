H, W = map(int,input().split())
for i in range(H):
    for j in range(W):
        output = 4
        if (i == 0 and i == H-1): output -= 2
        elif (i == 0 or i == H-1): output -= 1
        if (j == 0 and j == W-1): output -= 2
        elif (j == 0 or j == W-1): output -= 1
        print(output,end=" ")
    print("")