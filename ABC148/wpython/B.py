N = int(input())
S, T = input().split()
output = ""
for i in range(N):
    output += S[i] + T[i]
print(output)