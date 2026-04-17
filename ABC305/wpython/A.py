N = int(input())
if N%5 < 5 - N%5:
    print(N - N%5)
else:
    print((N//5 + 1)*5)