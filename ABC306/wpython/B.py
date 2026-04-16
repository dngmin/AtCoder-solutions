A_list = list(map(int,input().split()))
n = 1
total = 0
for A in A_list:
    total += A*n
    n *=2
print(total)