N, P, Q, R, S = map(int,input().split())
A_list = list(map(int,input().split()))
new_list = A_list[:P-1] + A_list[R-1:S] + A_list[Q:R-1] + A_list[P-1:Q] + A_list[S:]
print(" ".join(map(str,new_list)))