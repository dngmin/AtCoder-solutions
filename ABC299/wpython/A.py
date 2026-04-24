N = int(input())
S = input()
between = False

for s in S:
    if s == '*':
        print("in" if between else "out")
        break
    if s == '|':
        between = False if between else True