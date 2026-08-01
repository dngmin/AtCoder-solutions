N = int(input())
k = 0
while 1:
    if 2 ** k <= N: k += 1
    else: break
print(k-1)