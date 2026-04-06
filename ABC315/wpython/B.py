M = int(input())
days = list(map(int,input().split()))
middle = (sum(days) + 1) // 2
month = 1
for day in days:
    if middle <= day:
        print(month, middle)
        break
    else:
        month+=1
        middle -= day