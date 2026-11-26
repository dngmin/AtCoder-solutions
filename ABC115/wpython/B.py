N = int(input())
p_list = list()
for _ in range(N):
    p_list.append(int(input()))
print(sum(p_list) - max(p_list)//2)