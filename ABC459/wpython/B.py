N = int(input())
S_list = list(input().split())
output = ""
sample = "22233344455566677778889999"
for S in S_list:
    c = S[0]
    output += sample[ord(c) - ord('a')]
print(output)