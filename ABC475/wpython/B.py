N = int(input())
one = 0
ten = 0
hun = 0
for A in list(map(int,input().split())):
    if A % 1000 == 0: continue
    change = 1000 - A%1000
    hun += change // 100
    ten += (change % 100) // 10
    one += change % 10
print(one, ten, hun)