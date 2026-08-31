N, X = map(int,input().split())
drunk = 0
for i in range(N):
    V, P = map(int,input().split())
    drunk += V * P
    if drunk > X * 100:
        print(i+1)
        break
else:
    print(-1)