n = int(input())
A_list = list(map(int,input().split()))
bases = [0,0,0,0]
P = 0
for A in A_list:
    bases[0] = 1
    for i in [3,2,1,0]:
        if bases[i]:
            bases[i] = 0
            if i+A > 3:
                P += 1
            else:
                bases[i+A] = 1
print(P)