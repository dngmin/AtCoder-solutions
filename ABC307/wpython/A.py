N = int(input())
A_list = list(map(int,input().split()))
output = list()
week_total = 0
i = 0
for A in A_list:
    week_total += A
    i += 1

    if i == 7:
        output.append(week_total)
        week_total, i = 0, 0
print(" ".join(map(str,output)))