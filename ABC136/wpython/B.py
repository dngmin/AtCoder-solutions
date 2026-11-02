N = int(input())
for exponent in range(1,7):
    if N <= 10**exponent-1:
        break
if exponent == 1: print(N)
elif exponent == 2: print(9)
elif exponent == 3: print(N - 90)
elif exponent == 4: print(909)
elif exponent == 5: print(N - 9090)
else: print(90909)