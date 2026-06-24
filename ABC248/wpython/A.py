S = input()
n = [0] * 10
for s in S:
    n[int(s)] = 1
for i in range(10):
    if not n[i]:
        print(i)
        break