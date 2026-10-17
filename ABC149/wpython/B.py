A, B, K = map(int,input().split())
if K > A:
    print(0, max(0, A + B - K))
else:
    print(A-K, B)