abc = "abcdefghijklmnopqrstuvwxyz"
S = input()
T = input()
interval = 0
while (abc.find(S[0]) + interval) % 26 != abc.find(T[0]):
    interval += 1
for i in range(len(S)):
    if (abc.find(S[i]) + interval) % 26 != abc.find(T[i]):
        print("No")
        break
else:
    print("Yes")