N, M, T = map(int,input().split())
B_now = N
T_now = 0
for _ in range(M):
    A, B = map(int,input().split())
    B_now -= A - T_now
    if B_now <= 0:
        print("No")
        break
    B_now = min((B_now + B-A), N)
    T_now = B
else:
    print("Yes" if B_now - (T - T_now) > 0 else "No")