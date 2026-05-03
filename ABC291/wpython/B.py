N = int(input())
X_list = list(map(int,input().split()))
X_list.sort()
print(sum(X_list[N:4*N]) / (3*N))