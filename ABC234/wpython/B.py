N = int(input())
points_list = list()
for _ in range(N):
    point = list(map(int,input().split()))
    points_list.append(point)
maximum = 0
for x1, y1 in points_list:
    for x2, y2 in points_list:
        lenth = ((x1-x2)**2 + (y1-y2)**2)**0.5
        if lenth >= maximum:maximum = lenth
print(maximum)