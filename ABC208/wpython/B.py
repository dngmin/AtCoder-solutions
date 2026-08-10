P = int(input())
output = 0
f = 1
for i in range(1, 11):
    f *= i
for i in range(10,0,-1):
    n = P // f
    P -= n * f
    output += n
    f //= i
print(output)