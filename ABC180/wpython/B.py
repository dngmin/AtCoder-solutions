N = int(input())
x_list = list(map(int,input().split()))
Manhattan = 0
Euclidian = 0
Chebyshev = 0
for x in x_list:
    Manhattan += abs(x)
    Euclidian += x*x
    Chebyshev = max(abs(x), Chebyshev)
print(Manhattan)
print(Euclidian**0.5)
print(Chebyshev)