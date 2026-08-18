N = int(input())
highest = ["Name", 0]
second = ["Name", -1]
for _ in range(N):
    S, T = input().split()
    T = int(T)
    if T > highest[1]:
        second = highest
        highest = [S, T]
    elif T > second[1]:
        second = [S, T]
print(second[0])