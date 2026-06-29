N, T = int(input()), input()
x, y, way = 0, 0, "E"
for t in T:
    if t == "S":
        if way == "E": x += 1
        elif way == "S": y -= 1
        elif way == "W": x -= 1
        elif way == "N": y += 1
    else:
        if way == "E": way = "S" 
        elif way == "S": way = "W"
        elif way == "W": way = "N"
        elif way == "N": way = "E"
print(x, y)