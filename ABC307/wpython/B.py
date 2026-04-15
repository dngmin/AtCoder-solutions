N = int(input())
S_list = list(input() for _ in range(N))

for Si in S_list:
    for Sj in S_list:
        if Si == Sj:
            continue
        merge = Si+Sj
        lenth = len(merge)
        condition = True
        for i in range(lenth):
            if merge[i] != merge[lenth-1-i]:
                condition = False
        if condition:
            print("Yes")
            exit()
print("No")