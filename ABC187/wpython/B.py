N = int(input())
dot_x = list()
dot_y = list()
output = 0
for _ in range(N):
    x, y = map(int,input().split())
    dot_x.append(x)
    dot_y.append(y)
for i in range(N-1):
    for j in range(i+1,N):
        if -1 <= (dot_y[i] - dot_y[j]) / (dot_x[i] - dot_x[j]) <= 1:
            output += 1
print(output)