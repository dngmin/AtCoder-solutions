K = int(input())
A_list = list(map(int,input().split()))
print(min(A_list) if 9 in A_list else -1)