N = int(input())
for X in list(map(int,input().split())):
    if X >= 0:
        print("No")
        break
else:
    print("Yes")