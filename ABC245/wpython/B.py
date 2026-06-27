N = int(input())
A_list = list(map(int,input().split()))
all = [True] * 2001
for A in A_list:
    all[A] = False
for i in range(2001):
    if all[i]:
        print(i)
        break