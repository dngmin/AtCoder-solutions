N = int(input())
sum_inverse = 0
for A in list(map(int,input().split())):
    sum_inverse += 1 / A
print(1 / sum_inverse)