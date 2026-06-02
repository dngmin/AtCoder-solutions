S = input()
line = [True] * 7
if S[0] == "0":
    if "0" == S[6]: line[0] = False
    if "0" == S[3]: line[1] = False
    if S[1] == S[7] == "0": line[2] = False
    if S[0] == S[4] == "0": line[3] = False
    if S[2] == S[8] == "0": line[4] = False
    if "0" == S[5]: line[5] = False
    if "0" == S[9]: line[6] = False

    for i in range(5):
        for j in range(i+2,7):
            if line[i] == line[j] == True:
                if line[i+1:j] == [False] * (j - i - 1):
                    print("Yes")
                    exit()
print("No")