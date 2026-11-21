N = int(input())
total = 0
for _ in range(N):
    x, u = input().split()
    total += float(x) * (1 if u == "JPY" else 380000)
print(total)