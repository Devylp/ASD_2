coins = [1, 2, 5, 10] # Номиналы монет
result_coins = []
amount = int(input("Введите сумму сдачи: "))

map = [10_000_000]*(amount + 1)
map[0] = 0

for i in range(1, amount + 1):
    for coin in coins:

        if i - coin >= 0:
            res = map[i - coin] + 1

            if res < map[i]:
                map[i] = res
                result_coins.append(coin)

result = map[amount]

if result == 10_000_000:
    print(f"Для клиента размен сдачи: {amount}\nНевозможен")

print(f"Клиенту необходимо выдать сдачу в размере: {amount}\nколичеством монет: {result}") # \nМонетами номиналом: {result_coins}