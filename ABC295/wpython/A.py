eng = {"and", "not", "that", "the", "you"}
N = int(input())
W_list = list(input().split())
for W in W_list:
    if W in eng:
        print("Yes")
        break
else:
    print("No")