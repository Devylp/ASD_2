sample_text = 'AAABBCCABCCABCCCB'
sample_search = 'ABC'
n = len(sample_search)

# Создаем алфавит из исходного строки/текста
alphabet = sorted(list(set(sample_text)))
char_to_idx = {char: i for i, char in enumerate(alphabet)} # Требуется для навигации при построении таблицы переходов, чтобы не было Table[0]['A']
table_of_transition = [[0] * len(alphabet) for _ in range(n + 1)]

for i in range(n + 1):
    for char in alphabet:
        # Срезы потребуются для определения следующего состояния 
        # на основе префиксов шаблона и суффиксов входной строки + какой-то символ (в нашем случае char)
        current_str = sample_search[:i] + char

        q = i + 1 
        while q > 0:
            if sample_search[:q] == current_str[-q:]:
                break
            q -= 1  

        table_of_transition[i][char_to_idx[char]] = q


def Search_text(text, sub_text):
    m = len(text)
    n = len(sub_text)
    q = 0
    for i in range(m):
        q = table_of_transition[q][char_to_idx[text[i]]]

        if q == n:
            return i - n + 1
    
    return None


result = Search_text(sample_text, sample_search)
if result is not None:
    print(f'Был найден\nПаттерн: {sample_search}\nВ исходном тексте: {sample_text}')
else:
    print(f'Не был найден\nПаттерн: {sample_search}\nВ исходном тексте: {sample_text}')