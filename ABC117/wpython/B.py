N = int(input())
L_list = list(map(int,input().split()))
print("Yes" if sum(L_list) > 2*max(L_list) else "No")