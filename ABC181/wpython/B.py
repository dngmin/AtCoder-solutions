N = int(input())
output = 0
for _ in range(N):
    A, B = map(int,input().split())
    output += B*(B+1)//2 - A*(A-1)//2
print(output)