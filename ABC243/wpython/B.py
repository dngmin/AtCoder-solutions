N = int(input())
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))
output1 = 0
output2 = 0
for i in range(N):
    A = A_list[i]
    B = B_list[i]
    if A == B:
        output1 += 1
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if A_list[i] == B_list[j]:
            output2 += 1
print(output1)
print(output2)
        