N, M = map(int,input().split())
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))
for B in B_list:
    if B in A_list:
        A_list.pop(A_list.index(B))
    else:
        print("No")
        break
else:
    print("Yes")