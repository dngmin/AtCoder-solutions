A, B, W = map(int,input().split())
W *= 1000
M = W // A
m = W // B if W % B == 0 else W // B + 1
print(f"{m} {M}" if M >= m else "UNSATISFIABLE")