N = int(input())
H_list = list(map(int,input().split()))
count = 0
for i in range(N):
    for j in range(i):
        if H_list[i] < H_list[j]:
            break
    else:
        count += 1
print(count)