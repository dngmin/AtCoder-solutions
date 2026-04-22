N = int(input())
S = input()
T, A = 0, 0
for s in S:
    if s == "T":
        T += 1
    else:
        A += 1
if T > A:
    print("T")
elif T < A:
    print("A")
else:
    print("T" if s == "A" else "A")