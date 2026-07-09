N = int(input())
H_list = list(map(int,input().split()))
top = 0
for i in range(N):
    if H_list[i] > top:
        top = H_list[i]
    else:
        break
print(top)