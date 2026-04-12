T, X = map(int,input().split())
A_list = list(map(int,input().split()))
print(0,A_list[0])
pre_A = A_list[0]
for t in range(1,T+1):
    A = A_list[t]
    if abs(A - pre_A) >= X:
        print(t,A)
        pre_A = A