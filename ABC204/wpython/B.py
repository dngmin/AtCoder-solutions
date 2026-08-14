N = int(input())
A_list = list(map(int,input().split()))
output = 0
for A in A_list:
    output += A - 10 if A >= 10 else 0
print(output)