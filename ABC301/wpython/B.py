N = int(input())
A_list = list(map(int,input().split()))
for i in range(N-1):
    if A_list[i] - A_list[i+1] != 1:
        if A_list[i] > A_list[i+1]:
            for j in range(A_list[i], A_list[i+1],-1):
                print(j, end=" ")
        else:
            for j in range(A_list[i], A_list[i+1], 1):
                print(j, end=" ")
    else:
        print(A_list[i], end=" ")
print(A_list[-1])