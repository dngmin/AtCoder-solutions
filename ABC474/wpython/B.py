N = int(input())
P_list = list(map(int,input().split()))
n = N//10 if N%10 == 0 else N//10+1
for i in range(n):
    if i == n-1 and N%10 != 0:
        if set(range(i*10+1, i*10+1+N%10)) != set(P_list[i*10:]):
            print("No")
            break
    else:
        if set(range(i*10+1,(i+1)*10+1)) != set(P_list[i*10:(i+1)*10]):
            print("No")
            break
else:
    print("Yes")