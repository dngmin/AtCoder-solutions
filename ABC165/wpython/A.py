K = int(input())
A, B = map(int,input().split())
print("OK" if A <= (B//K) * K <= B else "NG")