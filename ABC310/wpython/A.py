N, P, Q = map(int,input().split())
D_list = list(map(int,input().split()))
print(P if P <= Q + min(D_list) else Q + min(D_list))