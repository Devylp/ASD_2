
# Сложность алгоритма префиксной функции составялет O(len(sample)), так как совершается единственный обход
# Оптимизация достигается за счёт использования предыдущего результата j = pi_array[j-1]

input_string = 'лилилось лилилась' #input("Введите исходный текст/строку: ")
Sample = 'лилила' #input("Введите строку для поиска: ")
m = len(Sample)
n = len(input_string)

p = [0]*len(Sample)
i = 1
j = 0

# Так как счетики i,j установлены вне цикла и должны меняться в условии, то естественно используем цикл while
while i < m:
    if Sample[j] == Sample[i]:
        p[i] = j+1
        i += 1
        j += 1
        
    # Ветка sample[j] != sample[i]
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j-1]


i = 0
j = 0
while i < n:
    if input_string[i] == Sample[j]:
        i += 1
        j += 1
        if j == m:
            print(f"Подстрока {Sample} найдена в исходной строке {input_string}")
            break
    
    # Ветка input_string[i] != sample[j]
    else:
        if j > 0:
            j = p[j-1]
        
        else:
            i += 1

    if i == n:
        print(f"Подстрока {Sample} не была найдена в исходной строке {input_string}")
    