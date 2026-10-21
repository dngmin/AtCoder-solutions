S = input()
len_s = len(S)
count = 0
for i in range(len_s//2):
    count += S[i] != S[-i-1]
print(count)