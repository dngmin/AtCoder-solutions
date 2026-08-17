S = input()
for i in range(len(S)):
    s = S[len(S) - i - 1]
    if s == "6":
        print("9", end= "")
    elif s == "9":
        print("6", end= "")
    else:
        print(s, end= "")