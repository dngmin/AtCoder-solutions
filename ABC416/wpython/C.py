N, K, X = map(int,input().split())
S_list = [input() for _ in range(N)]
all = list()

K -= 1
for S in S_list:
    all.append(S)

while K > 0:
    K -= 1
    new_all = list()
    for element in all:
        for S in S_list:
            new_all.append(element+S)
    all = new_all
all.sort()
print(all[X-1])