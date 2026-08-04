N = int(input())
A_list = list(map(int,input().split()))
last_idx, last = -1, -1
booby_idx, booby = -1, -1
for i in range(N):
    if A_list[i] > last:
        booby = last
        booby_idx = last_idx
        last = A_list[i]
        last_idx = i+1
    elif A_list[i] > booby:
        booby = A_list[i]
        booby_idx = i+1
print(booby_idx)