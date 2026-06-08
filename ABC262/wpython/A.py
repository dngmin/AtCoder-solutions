Y = int(input())
amari = Y%4
if amari <= 2:
    print(Y + 2 - amari)
else:
    print(Y + 6 - amari)