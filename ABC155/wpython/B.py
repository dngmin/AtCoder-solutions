N = int(input())
for A in list(map(int,input().split())):
    if A % 2 == 0:
        if A % 3 == 0 or A % 5 == 0:
            continue
        else:
            print("DENIED")
            break
else:
    print("APPROVED")