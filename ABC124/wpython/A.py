A, B = map(int,input().split())
C = max(A,B)
print(A+B if A == B else C+(C-1))