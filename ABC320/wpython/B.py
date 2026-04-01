S = input()
output = 1
for i in range(len(S)):
    for j in range(len(S)-i):
        string = S[j:j+i+1]
        reverse = string[::-1]
        if string == string[::-1] and i+1 > output:
            output = i+1
print(output)