judge = {"AC" : 0, "WA" : 0, "TLE" : 0, "RE" : 0}
for _ in range(int(input())):
    judge[input()] += 1
print("AC x",judge["AC"])
print("WA x",judge["WA"])
print("TLE x",judge["TLE"])
print("RE x",judge["RE"])