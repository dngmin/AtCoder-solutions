N = int(input())
p = list(map(int,input().split()))
swap = False
for i in range(N):
    if p[i] != i+1:
        if not swap and p[p[i]-1] == i+1:
            p[p[i]-1] = p[i]
            p[i] = i+1
            swap = True
            continue
        print("NO")
        break
else:
    print("YES")