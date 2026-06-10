N, X, Y, Z = map(int,input().split())
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))
passed = [False] * (N)
math_rank = list()
english_rank = list()
total_rank = list()
for i in range(N):
    math_rank.append([i, A_list[i]])
    english_rank.append([i, B_list[i]])
    total_rank.append([i, A_list[i] + B_list[i]])
math_rank.sort(key= lambda x: x[1], reverse= True)
english_rank.sort(key= lambda x: x[1], reverse= True)
total_rank.sort(key= lambda x: x[1], reverse= True)

count = 0
for i,m in math_rank:
    if count == X: break
    if not passed[i]:
        passed[i] = True
        count += 1
for i,m in english_rank:
    if count == X + Y: break
    if not passed[i]:
        passed[i] = True
        count += 1
for i,m in total_rank:
    if count == X + Y + Z: break
    if not passed[i]:
        passed[i] = True
        count += 1
for i, p in enumerate(passed):
    if p: print(i+1)