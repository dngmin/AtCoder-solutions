N = int(input())
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))
for i, B in enumerate(B_list, start = 1):
    if not A_list[B-1] == i:
        print("No")
        break
else:
    print("Yes")