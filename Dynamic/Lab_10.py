def Solution(Floors):
    drops = 1
    while (drops*(1 + drops))/2 < Floors:
        drops += 1
    
    return drops

eggs = int(input("Введите количество яиц: "))
floors = int(input("Введите количество этажей: "))

print(f"\nВ случае для: {eggs} яиц\nДля дома с количеством этажей: {floors}\nМинимальное количество бросков для классификации равно: {Solution(floors)}")