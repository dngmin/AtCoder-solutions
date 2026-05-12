T = int(input())
for _ in range(T):
    N = int(input())
    A_list = list(map(int,input().split()))
    output = 0
    for A in A_list:
        output += 1 if A%2 == 1 else 0
    print(output)