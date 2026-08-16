A, B = map(int,input().split())
p = A + B == 9
m = A - B == 9
M = A * B == 9
d = A / B == 9
print("Nine" if p or m or M or d else "Nein")