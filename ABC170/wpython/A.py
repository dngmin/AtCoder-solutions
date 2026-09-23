x_list = list(map(int,input().split()))
for i, x in enumerate(x_list):
    if x == 0:
        print(i+1)
        break