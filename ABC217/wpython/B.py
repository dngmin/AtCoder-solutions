contest = ord("B") + ord("R") + ord("G") + ord("H")
for _ in range(3):
    S = input()
    contest -= ord(S[1])
print("A"+chr(contest)+"C")