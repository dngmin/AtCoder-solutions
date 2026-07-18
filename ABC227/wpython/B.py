guaranteed = [False] * 1001
for a in range(1, 143):
    for b in range(1, 143):
        i = 4*a*b + 3*a + 3*b
        if i > 1000: break
        guaranteed[i] = True

N = int(input())
S_list = list(map(int,input().split()))
output = 0
for S in S_list:
    if not guaranteed[S]: output += 1
print(output)