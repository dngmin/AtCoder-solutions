N = int(input())
A_list = [list(map(int,input().split()))[1:] for _ in range(N)]
X, Y = map(int,input().split())
print(A_list[X-1][Y-1])