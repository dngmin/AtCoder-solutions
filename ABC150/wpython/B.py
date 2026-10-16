N = int(input())
S = input()
i = 0
count = 0
while i < N:
    if S[i:i+3] == "ABC":
        count += 1
        i += 3
    else:
        i += 1
print(count)