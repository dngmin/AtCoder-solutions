N, X = map(int,input().split())
A_total = sum(map(int,input().split()))
print("Yes" if A_total - N//2 <= X else "No")