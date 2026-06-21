N, X = input().split()
N = int(N)
X = "ABCDE".index(X)

for _ in range(N):
    S = input()
    if S[X] == "o":
        print("Yes")
        break
else:
    print("No")