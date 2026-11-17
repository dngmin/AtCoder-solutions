Antennas = list()
for i in range(5):
    Antennas.append(int(input()))
k = int(input())
print("Yay!" if Antennas[4] - Antennas[0] <= k else ":(")