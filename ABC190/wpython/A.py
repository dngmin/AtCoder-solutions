A, B, C = map(int,input().split())
if A == B: print("Takahashi" if C else "Aoki")
else: print("Takahashi" if A > B else "Aoki")