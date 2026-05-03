def Solution(Floors):
    drops = 1
    while (drops * (1 + drops)) // 2 < Floors:   # // для целочисленного деления
        drops += 1
    return drops

def get_first_egg_path(floors, drops):
    """
    Возвращает список этажей, с которых нужно бросать первое яйцо
    (оптимальная стратегия для двух яиц).
    """
    path = []
    current_floor = 0
    step = drops
    while current_floor < floors:
        next_floor = min(current_floor + step, floors)
        path.append(next_floor)
        current_floor = next_floor
        step -= 1
        if step == 0:      # на случай, когда сумма больше нужного, но мы упёрлись в конец
            break
    return path

eggs = 2
floors = int(input("Введите количество этажей: "))

min_drops = Solution(floors)
path = get_first_egg_path(floors, min_drops)

print(f"\nДля {eggs} яиц и {floors} этажей:")
print(f"Минимальное количество бросков в худшем случае: {min_drops}")
print(f"Путь (этажи для первого яйца): {path}")