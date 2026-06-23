A, B, C, D, E, F, X = map(int,input().split())
t = (X // (A + C)) * (A * B) + (A * B if X % (A + C) > A else (X % (A + C)) * B)
a = (X // (D + F)) * (D * E) + (D * E if X % (D + F) > D else (X % (D + F)) * E)
print("Draw" if t == a else "Takahashi" if t > a else "Aoki")
