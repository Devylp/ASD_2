from math import sqrt

'''
Записать алгоритмы: 
1. Нахождения точек пересечения двух прямых
2. Прямой и отрезка
3. Двух отрезков
4. Прямой и окружности
5. Отрезка и окружности
6. Двух окружностей
'''

def get_line(p1: tuple[float, float], p2: tuple[float, float]) -> tuple[float, float, float]:
    x1, y1 = p1
    x2, y2 = p2
    A = y1 - y2
    B = x2 - x1
    C = -A * x1 - B * y1
    return A, B, C

# 1.
def lines_crossing(line1: tuple[float, float, float], line2: tuple[float, float, float]) -> tuple[float, float] | None:
    A1, B1, C1 = line1
    A2, B2, C2 = line2

    main_determinant = A1*B2 - A2*B1
    x_determinant = B1*C2 - B2*C1
    y_determinant = A2*C1 - A1*C2

    # 1e-9 нужно для учета погрешностей в main_determinant (здесь условие параллельности и совпадения)
    if abs(main_determinant) < 1e-9:
        return None

    x = x_determinant / main_determinant
    y = y_determinant / main_determinant

    return (x, y)

# 2.
def line_and_segment_crossing(line: tuple[float, float, float], start: tuple[float, float], end: tuple[float, float]) -> tuple[float, float] | None:
    A, B, C = line
    x1, y1 = start
    x2, y2 = end

    value_1 = A*x1 + B*y1 + C
    value_2 = A*x2 + B*y2 + C

    if (value_1 * value_2) <= 1e-9:
        line_segment = get_line(end, start)
        return lines_crossing(line, line_segment)
    
    return None

# 3.
def segments_crossing(start1: tuple[float, float], end1: tuple[float, float], start2: tuple[float, float], end2: tuple[float, float]) -> tuple[float, float] | None:
    x1, y1 = start1; x2, y2 = end1
    x3, y3 = start2; x4, y4 = end2

    # Знаменатель (аналог определителя)
    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)

    if abs(denom) < 1e-9:
        return None  # Параллельны

    # Параметры пересечения t (для первого отрезка) и u (для второго)
    t = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    u = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom

    # Если 0 <= t <= 1 и 0 <= u <= 1, то пересечение внутри отрезков
    if 0 <= t <= 1 and 0 <= u <= 1:
        res_x = x1 + t * (x2 - x1)
        res_y = y1 + t * (y2 - y1)
        return (res_x, res_y)

    return None

# 4.
def line_and_circle_crossing(start: tuple[float, float], end: tuple[float, float], center: tuple[float, float], Radius: float):
    x1, y1 = start
    x2, y2 = end
    x_c, y_c = center
    R = Radius
    result = []

    dx = x2 - x1
    dy = y2 - y1

    a = dx**2 + dy**2
    b = 2 * (dx * (x1 - x_c) + dy * (y1 - y_c))
    c = (x1 - x_c)**2 + (y1 - y_c)**2 - R**2

    D = sqrt(b**2 - 4 * a * c)

    # Дискриминант отрицательный, следовательно прямая не пересекает окружность
    if D < -1e-9:
        return []
    
    sqrt_D = 0 if abs(D) < 1e-9 else sqrt(D)

    t1 = (-b + sqrt_D) / (2 * a)
    t2 = (-b - sqrt_D) / (2 * a)

    # Переводим параметры t обратно в координаты (x, y)
    res_x1 = x1 + t1 * dx
    res_y1 = y1 + t1 * dy
    result.append((res_x1, res_y1))

    # Если это не касание (дискриминант явно больше нуля), добавляем вторую точку
    if D > 1e-9:
        res_x2 = x1 + t2 * dx
        res_y2 = y1 + t2 * dy
        result.append((res_x2, res_y2))

    return result



# 5.
def segment_and_circle_crossing(start: tuple[float, float], end: tuple[float, float], center: tuple[float, float], Radius: float) -> list[tuple[float, float]]:
    x1, y1 = start
    x2, y2 = end
    x_c, y_c = center
    R = Radius
    
    dx, dy = x2 - x1, y2 - y1
    
    # Твои коэффициенты из 4-й задачи
    a = dx**2 + dy**2
    b = 2 * (dx * (x1 - x_c) + dy * (y1 - y_c))
    c = (x1 - x_c)**2 + (y1 - y_c)**2 - R**2
    
    D = b**2 - 4 * a * c
    if D < -1e-9: return []
    
    sqrt_D = 0 if D < 1e-9 else sqrt(D)
    t_values = [(-b + sqrt_D) / (2 * a), (-b - sqrt_D) / (2 * a)]
    
    points = []
    # Проверяем, что точка пересечения попала на отрезок
    # Используем множество или проверку t1 != t2, чтобы не дублировать точку касания
    seen_t = set() 
    for t in t_values:
        if 0 - 1e-9 <= t <= 1 + 1e-9:
            # Округляем t, чтобы не добавить одну и ту же точку касания дважды
            rounded_t = round(t, 9)
            if rounded_t not in seen_t:
                points.append((x1 + t * dx, y1 + t * dy))
                seen_t.add(rounded_t)
    return points

# 6.
def two_circles_crossing(center1: tuple[float, float], Radius_1: float, center2: tuple[float, float], Radius_2: float):
    x1, y1 = center1
    x2, y2 = center2
    R_1 = Radius_1
    R_2 = Radius_2
    
    # Расстояние между центрами
    d = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Проверки: слишком далеко или одна внутри другой
    if d > R_1 + R_2 + 1e-9 or d < abs(R_1 - R_2) - 1e-9:
        return []
        
    # Коэффициенты радикальной оси Ax + By + C = 0
    A = 2 * (x2 - x1)
    B = 2 * (y2 - y1)
    C = x1**2 + y1**2 - R_1**2 - x2**2 - y2**2 + R_2**2
    
    # Получаем две точки на этой прямой, чтобы вызвать функцию 4
    if abs(B) > abs(A):
        # Прямая не вертикальная, берем x=0 и x=1
        p1 = (0, -C / B)
        p2 = (1, (-C - A) / B)
    else:
        # Прямая вертикальная, берем y=0 и y=1
        p1 = (-C / A, 0)
        p2 = ((-C - B) / A, 1)
        
    # Просто вызываем твою 4-ю функцию для первой окружности и этой прямой
    return line_and_circle_crossing(p1, p2, center1, Radius_1)




def run_tests():
    print("--- Тестирование геометрических функций ---")

    # 1. Пересечение двух прямых (X-образное пересечение в (0,0))
    # Прямые: x - y = 0 и x + y = 0
    l1, l2 = (1, -1, 0), (1, 1, 0)
    print(f"1. Прямые: {lines_crossing(l1, l2)} (Ожидается: (0.0, 0.0))")

    # 2. Прямая и отрезок
    # Прямая y = 5, отрезок от (0,0) до (0,10). Пересечение в (0,5)
    line = (0, 1, -5)
    p1, p2 = (0, 0), (0, 10)
    print(f"2. Прямая и отрезок: {line_and_segment_crossing(line, p1, p2)} (Ожидается: (0.0, 5.0))")

    # 3. Два отрезка (Крест)
    # Отрезок1: (0,0)-(2,2), Отрезок2: (0,2)-(2,0). Пересечение в (1,1)
    s1_a, s1_b = (0, 0), (2, 2)
    s2_a, s2_b = (0, 2), (2, 0)
    print(f"3. Два отрезка: {segments_crossing(s1_a, s1_b, s2_a, s2_b)} (Ожидается: (1.0, 1.0))")

    # 4. Прямая и окружность
    # Прямая x = 3, окружность в (0,0) R=5. Точки: (3, 4) и (3, -4)
    p_a, p_b = (3, 0), (3, 10)
    center, radius = (0, 0), 5
    print(f"4. Прямая и окружность: {line_and_circle_crossing(p_a, p_b, center, radius)} (Ожидается: 2 точки)")

    # 5. Отрезок и окружность
    # Отрезок (0,0)-(2,0), окружность в (3,0) R=2. Пересечение только в (1,0)
    s_start, s_end = (0, 0), (2, 0)
    c_5, r_5 = (3, 0), 2
    print(f"5. Отрезок и окружность: {segment_and_circle_crossing(s_start, s_end, c_5, r_5)} (Ожидается: (1.0, 0.0))")

    # 6. Две окружности
    # Окр1: центр(0,0) R=2, Окр2: центр(2,0) R=2. 
    # Пересекаются в (1, 1.732) и (1, -1.732)
    c1, r1 = (0, 0), 2
    c2, r2 = (2, 0), 2
    print(f"6. Две окружности: {two_circles_crossing(c1, r1, c2, r2)} (Ожидается: 2 точки, x=1.0)")


run_tests()