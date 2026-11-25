s = int(input())
count = dict()
m = 1
while True:
    try:
        if count[s]:
            print(m)
            break
    except:
        count[s] = True
    m += 1
    s = s//2 if s%2 == 0 else 3*s + 1