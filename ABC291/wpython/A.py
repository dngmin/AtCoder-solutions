S = input()
for i in range(len(S)):
    if 65 <= ord(S[i]) <= 90:
        print(i+1)
        break