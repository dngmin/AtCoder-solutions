N = int(input())
degrees = list(map(int,input().split()))
total = sum(degrees)
sliced = list()
for d in degrees:
    sliced.append(total%360)
    total -= d
sliced.sort()
sliced.append(360)
max_size = 0
start_dgree = 0
for d in sliced:
    size = d - start_dgree
    if size > max_size:
        max_size = size
    start_dgree = d
print(max_size)