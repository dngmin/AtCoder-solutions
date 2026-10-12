N = int(input())
S = input()
longest = 0
current = 0
for s in S:
    if s == "R":
        current += 1
    else:
        longest = max(longest, current)
        current = 0
print(max(longest,current))