N = int(input())
A = list(map(int,input().split()))
output = 0
for i in range(N-2):
    if A[i] < A[i+1] > A[i+2]:
        output += 1
print(output)