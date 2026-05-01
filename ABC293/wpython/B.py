N = int(input())
X_list = list(map(int,input().split()))
called = [0]*(N)
for i in range(N):
    if called[i]:
        continue
    else:
        called[X_list[i]-1] = 1
print(called.count(0))
for i in range(N):
    if not called[i]:
        print(i+1, end=" ")