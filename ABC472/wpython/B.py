N = int(input())
L_list = list(map(int,input().split()))
lenth = sum(L_list)
front = 0
output = 1e8
for L in L_list:
    front += L
    diff = lenth - front - front
    if (diff) * (diff) < output * output:
        output = diff
print(abs(output))