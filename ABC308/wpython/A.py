S_list = list(map(int,input().split()))
pre_S = 0
for S in S_list:
    if S >= pre_S and 100 <= S <= 675 and S%5 == 0:
        pre_S = S
        continue
    else:
        print("No")
        break
else:
    print("Yes")