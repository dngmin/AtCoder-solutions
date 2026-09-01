N = int(input())
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))
I = 0
for i in range(N):
    I += A_list[i] * B_list[i]
print("Yes" if I == 0 else "No")