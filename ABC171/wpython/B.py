N, K = map(int,input().split())
p_list = sorted(list(map(int,input().split())))
print(sum(p_list[:K]))