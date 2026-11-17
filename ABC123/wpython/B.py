dishes = list()
last_dish = 9
last_dish_index = -1
time = 0
for i in range(5):
    d = int(input())
    dishes.append(d)
    if d % 10 != 0 and d % 10 <= last_dish % 10:
        last_dish = d
        last_dish_index = i
if last_dish_index != -1:
    dishes.pop(last_dish_index)
for dish in dishes:
    time += dish//10 if dish%10 == 0 else dish//10 + 1
print(time*10 + (last_dish if last_dish_index != -1 else 0))