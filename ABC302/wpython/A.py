A, B = map(int,input().split())
if A < B:
    print(1)
elif A % B == 0:
    print(A//B)
else:
    print(A//B+1)