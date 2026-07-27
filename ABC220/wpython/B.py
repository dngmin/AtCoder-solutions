K = int(input())
A, B = map(int, input().split())
A_10, B_10 = 0, 0
i = 0
while A > 0:
    A_10 += (A % 10) * (K ** i)
    A //= 10
    i += 1
i = 0
while B > 0:
    B_10 += (B % 10) * (K ** i)
    B //= 10
    i += 1
print(A_10 * B_10)