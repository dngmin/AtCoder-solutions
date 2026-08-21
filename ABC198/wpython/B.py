N = input()
i = len(N) - 1
while N[i] == "0" and N != "0":
    N = '0' + N
l = len(N)
for i in range(l):
    if N[i] != N[l-1-i]:
        print("No")
        break
else:
    print("Yes")