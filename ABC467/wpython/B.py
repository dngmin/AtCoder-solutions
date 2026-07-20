N = int(input())
money = 1000
take_all = 1000
for _ in range(N):
    A, B, S = input().split()
    if S == "take": money -= int(A)
    else: money -= int(B)
    take_all -= int(A)
print(take_all - money)