N = int(input())
double = 0
for _ in range(N):
    D1, D2 = map(int,input().split())
    if D1 == D2: double += 1
    else: double = 0
    if double == 3:
        print("Yes")
        break
else:
    print("No")