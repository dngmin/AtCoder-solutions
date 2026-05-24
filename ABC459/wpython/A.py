S = "HelloWorld"
X = int(input())
for i in range(10):
    if (i+1 == X): continue
    print(S[i], end="")