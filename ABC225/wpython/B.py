N = int(input())
A, B = map(int,input().split())
for _ in range(N-2):
    ab = list(map(int,input().split()))
    if not A in ab: A = False
    if not B in ab: B = False
    if not A and not B:
        break
print("No" if not A and not B else "Yes")