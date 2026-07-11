X, Y = map(int,input().split())
if X >= Y: output = 0
else:
    output = (Y - X) // 10
    if (Y - X) % 10:
        output += 1
print(output)