N = int(input())
H_list = list(map(int,input().split()))
takahashi = -1
takahashi_index = -1
for i, H in enumerate(H_list):
    if H > takahashi:
        takahashi = H
        takahashi_index = i + 1
print(takahashi_index)