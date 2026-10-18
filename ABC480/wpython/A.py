row1 = input()
row2 = input()
AD = ["AD", "DA"]
if row1[0] + row2[1] in AD:
    print("No")
elif row1[1] + row2[0] in AD:
    print("No")
else:
    print("Yes")