S = input()
T = input()
output = 0
for i in range(3):
    output += S[i] == T[i]
print(output)