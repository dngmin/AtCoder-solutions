A, B, C, D = map(int,input().split())
Takahashi = A//D + (0 if A % D == 0 else 1)
Aoki = C//B + (0 if C % B == 0 else 1)
print("Yes" if Takahashi >= Aoki else "No")