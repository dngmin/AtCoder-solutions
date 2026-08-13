N = int(input())
A_set = set(map(int,input().split()))
standard = set(range(1,N+1))
print("Yes" if A_set & standard == standard else "No")