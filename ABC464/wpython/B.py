H, W = map(int,input().split())
screen = list(input() for _ in range(H))
l, r, u, d = 0, W, 0, H

for i in range(d):
    if screen[i] == "." * W:
        u += 1
    else:
        break
for i in range(d-1,u,-1):
    if screen[i] == "." * W:
        d -= 1
    else:
        break
for i in range(l,r):
    for row in screen[u:d]:
        if row[i] == "#":
            break
    else:
        l += 1
        continue
    break
for i in range(r-1,l,-1):
    for row in screen[u:d]:
        if row[i] == "#":
            break
    else:
        r -= 1
        continue
    break

for i in range(u, d):
    print(screen[i][l:r])