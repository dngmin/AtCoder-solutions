N = int(input())
A_list = list(map(int,input().split()))
Q = int(input())
for _ in range(Q):
    query = input()
    if query[0] == '1':
        _, k, x = map(int,query.split())
        A_list[k-1] = x
    else:
        _, k = map(int,query.split())
        print(A_list[k-1])