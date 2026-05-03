# Ввод данных
N, M = [int(x) for x in input().split()]
m = [0] + [int(x) for x in input().split()]   # веса
c = [0] + [int(x) for x in input().split()]   # стоимости

# dp[i][j] – макс. стоимость для i предметов и вместимости j
dp = [[0] * (M + 1) for _ in range(N + 1)]

# Заполнение таблицы
for i in range(1, N + 1):
    for j in range(0, M + 1):
        dp[i][j] = dp[i - 1][j]                     # не берём
        if m[i] <= j:
            # если берём – лучше?
            dp[i][j] = max(dp[i][j], dp[i - 1][j - m[i]] + c[i])


# Максимальная стоимость (на самом деле dp[N][M], но max(dp[N]) надёжнее)
max_value = max(dp[N])
print(f"Максимальная стоимость: {max_value}")



# Восстановление выбранных предметов
selected_items = []   # список индексов взятых предметов
j = M                 # начинаем с полной вместимости

# Идём от последнего предмета к первому
for i in range(N, 0, -1):
    # Если значение такое же, как без этого предмета – мы его не брали
    if dp[i][j] == dp[i - 1][j]:
        continue      # пропускаем, j остаётся тем же
    else:
        # Иначе предмет i точно взяли
        selected_items.append(i)
        j -= m[i]     # уменьшаем оставшуюся вместимость

# Список восстановлен в обратном порядке, перевернём
selected_items.reverse()



# Вывод подробностей
print("Выбранные предметы (индекс, вес, стоимость):")
total_weight = 0
total_cost = 0
for idx in selected_items:
    print(f"  Предмет {idx}: вес = {m[idx]}, стоимость = {c[idx]}")
    total_weight += m[idx]
    total_cost += c[idx]

print(f"Суммарный вес: {total_weight}")
print(f"Суммарная стоимость: {total_cost}")


'''
4 6
2 4 1 2
7 2 5 1
'''