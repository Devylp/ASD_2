list = [12, -9, 20, 0, 1, -17, 4, -1]
max_val = 0

map = [0]*len(list)
map[0] = list[0]
i = 1
temp_start = 0
best_start = 0
best_end = 0

while i < len(list):
    if map[i-1] + list[i] > list[i]:
        map[i] = map[i-1] + list[i]

    else:
        map[i] = list[i]
        temp_start = i

    if map[i] > max_val:
        max_val = map[i]
        best_start = temp_start
        best_end = i

    i += 1


print(f"Для массива максимальной длины: {list[best_start:best_end+1]}\nИсходного массива: {list}\nНаибольшая сумма равна: {max_val}")