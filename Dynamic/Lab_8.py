def get_all_combinations(amount, coins=[1, 2, 5, 10]):
    """
    Возвращает список всех уникальных комбинаций монет,
    дающих в сумме amount (порядок монет не важен).
    Каждая комбинация — список монет (например, [5, 2, 2, 1]).
    """

    coins = sorted(coins, reverse=True)
    result = []

    def backtrack(remaining, index, current_combination):
        if remaining == 0:
            result.append(current_combination[:])  #нашли комбинацию
            return
        if index == len(coins):
            return  # монеты кончились

        # Пробуем взять 0, 1, 2,... монет текущего номинала
        coin = coins[index]
        max_count = remaining // coin
        for count in range(max_count + 1):
            # добавляем count монет в комбинацию
            for _ in range(count):
                current_combination.append(coin)
            # рекурсивно заполняем оставшуюся сумму следующими (меньшими) монетами
            backtrack(remaining - coin * count, index + 1, current_combination)
            # откатываем добавленные монеты
            for _ in range(count):
                current_combination.pop()

    backtrack(amount, 0, [])
    return result


if __name__ == "__main__":
    # Демонстрация на небольшой сумме
    test_amount = 17
    combinations = get_all_combinations(test_amount)

    print(f"Сумма: {test_amount}")
    print(f"Всего способов: {len(combinations)}")
    print("Примеры комбинаций:")
    for combo in combinations:
        print(combo)