N = int(input())
A_list = list(map(int,input().split()))
for A in A_list:
    if A%2 == 0:
        print(A, end=" ")