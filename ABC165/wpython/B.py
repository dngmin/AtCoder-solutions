X = int(input())
yen = 100
year = 0
while X > yen:
    yen += yen // 100
    year += 1
print(year)