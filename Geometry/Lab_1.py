import math

# Функция для нахождения косоугольного(псевдоскалярного) произведения AB на BC
def Get_Oblique_Product(A, B, C):
    return (B[0] - A[0])*(C[1] - B[1]) - (C[0] - B[0])*(B[1] - A[1])

# 1. Формат ввода - строка, где координаты точки разделены пробелом
input_string_points = input("Введите координаты точек строго в формате x,y z,w: ")

list_points = [tuple(map(float, point.split(','))) for point in input_string_points.split() if ',' in point]

# 2. Поиск искусственного центра оболочки (координаты центра - это среднее арифметическое всех входных точек)
sum_x = 0.0
sum_y = 0.0

for pnt in list_points:
    sum_x += pnt[0]
    sum_y += pnt[1]

count = len(list_points)
center = (sum_x / count, sum_y / count)


# 3. Производим сканирование относительно центра (используем полярную систему координат)
scanned_points = []
for pnt1 in list_points:
    delta_x = pnt1[0] - center[0]
    delta_y = pnt1[1] - center[1]

    # 3.1 Считаем полярный угол и радиус
    polar_angle = math.atan2(delta_y, delta_x)
    polar_radius = math.hypot(delta_x, delta_y)
    scanned_points.append((polar_angle, polar_radius, pnt1))


# 3.2 Сортируем отсканированные точки
scanned_points.sort()
sorted_points = [new_pnt[2] for new_pnt in scanned_points]


# 4. Обход точек с помощью стека, что определить их ориентацию (правая/левая или прямая тройка точек)
stack = [sorted_points[0], sorted_points[1]]

for i in range(2, len(sorted_points)):
    new_point = sorted_points[i]

    while len(stack) >= 2 and Get_Oblique_Product(stack[-2], stack[-1], new_point) <= 0:
        stack.pop()
    
    stack.append(new_point)


# 5. Вывод результата
# Тестовые данные: 34,66 67,89 90,3 23,56 12,34 68,99 1,10 11,0

if len(stack) >= 3: # 3 - это минимум для задания замкнутой оболочки
    print(f"\nВыпуклая оболочка существует.")
    print(f"Количество вершин: {len(stack)}")
    print("Координаты вершин:", stack)
else:
    print("\nВыпуклая оболочка не существует (точки вырождены в линию или точку).")