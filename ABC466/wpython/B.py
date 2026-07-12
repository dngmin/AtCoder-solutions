N, M = map(int,input().split())
color = [-1] * (M+1)
for _ in range(N):
    C, S = map(int,input().split())
    if S > color[C]: color[C] = S
print(*color[1:])