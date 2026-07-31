N = int(input())
name = list()
for _ in range(N):
    full_name = input()
    if full_name in name:
        print("Yes")
        break
    else:
        name.append(full_name)
else:
    print("No")