N, M = map(int,input().split())
foods = [0]*(M+1)
for _ in range(N):
    A_list = list(map(int,input().split()))
    for k in range(1,A_list[0]+1):
        foods[A_list[k]] += 1
print(foods.count(N))