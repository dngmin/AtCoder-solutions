N = int(input())
for i in range(1,8):
    if 10**(i+2) <= N <= 10**(i+3) - 1:
        print((N//10**i)*10**i)
        break
else:
    print(N)