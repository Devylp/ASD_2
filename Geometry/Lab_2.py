import sys

def Get_Oblique_Product(A, B, C):
    return (B[0] - A[0])*(C[1] - B[1]) - (C[0] - B[0])*(B[1] - A[1])

def is_inside(A, B, C, Point):
    # Эти переменные хранят значения и местопложении Point относительно каждой из сторон треугольника ABC
    half_plane_1 = Get_Oblique_Product(A, B, Point)
    half_plane_2 = Get_Oblique_Product(B, C, Point)
    half_plane_3 = Get_Oblique_Product(C, A, Point)

    # Проверка на вложенность точки в треугольник ABC
    if (half_plane_1 * half_plane_2 > 0) and (half_plane_2 * half_plane_3 > 0):
        return True
    return False

# 1. Формат ввода - строка, где координаты точки разделены пробелом
input_string_points = input("Введите координаты точек строго в формате x,y z,w: ")

list_points = [tuple(map(float, point.split(','))) for point in input_string_points.split() if ',' in point]


n = len(list_points)
found = False

# Проходимся по всем точкам
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # Точки внешнего треугольника
            A, B, C = list_points[i], list_points[j], list_points[k]
            
            # Проверка, что ABC не треугольник, а прямая в нашем случае
            if Get_Oblique_Product(A, B, C) == 0:
                continue
            
            # Поиск вложенных треугольников
            in_points = []
            for m in range(n):
                # Проверка, что точка уникальна (то есть не является хотя бы A, B, C)
                if m == i or m == j or m == k:
                    continue
                
                if is_inside(A, B, C, list_points[m]):
                    in_points.append(list_points[m])
            
            if len(in_points) >= 3:
                point_1, point_2 = in_points[0], in_points[1]
                
                if any(Get_Oblique_Product(in_points[0], in_points[1], in_point) != 0 for in_point in in_points[2:]):
                    print("Вложенные треугольники существуют")
                    sys.exit()

print("Вложенных треугольниклв не существует")