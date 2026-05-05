N, K = map(int,input().split())
S = input()
final = 0
for s in S:
    if s == "o" and final != K:
        final += 1
        print("o", end="")
    else:
        print("x", end="")