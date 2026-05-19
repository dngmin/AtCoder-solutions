H, M = map(int,input().split())
A, B = H // 10, H % 10
C, D = M // 10, M % 10
while (not 10*A + C < 24) or (not 10*B + D < 60):
    D += 1
    if D == 10:
        C += 1
        D = 0
    if C == 6:
        B += 1
        C = 0
    if B == 10:
        A += 1
        B = 0
    if 10 * A + B == 24:
        A, B = 0, 0
print(10*A+B, 10*C+D)