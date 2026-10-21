N = int(input())
S = input()
for s in S:
    s_idx = ord(s) + N
    if s_idx > 90: s_idx -= 26
    print(chr(s_idx), end="")