N, A, B = map(int,input().split())
index = list(map(int,input().split()))
AB = A+B
for i in range(N):
    if index[i] == AB:
        print(i+1)
        break