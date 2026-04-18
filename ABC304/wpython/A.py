N = int(input())
names = list()
youngest = 10**9
start = False
for i in range(N):
    S, A = input().split()
    names.append(S)
    A = int(A)
    if A < youngest:
        youngest = A
        start = i
for i in range(N):
    print(names[(start+i)%N])