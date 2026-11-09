N, X = map(int,input().split())
x_curr = 0
count = 1
for L in list(map(int,input().split())):
    x_curr += L
    if x_curr <= X:
        count += 1
    else: break
print(count)