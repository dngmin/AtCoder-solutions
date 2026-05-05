N, M = map(int,input().split())
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))
output = 0
for B in B_list:
    output += A_list[B-1]
print(output)