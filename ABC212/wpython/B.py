num = "0123456789012"
pw = input()
if pw[0]*4 == pw or num.find(pw) != -1:
    print("Weak")
else:
    print("Strong")