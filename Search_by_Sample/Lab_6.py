def Gorner_scheme(text):
    result = ord(text[0])
    base = 31
    for i in range(len(text) - 1):
        result = result * base + ord(text[i + 1])
    return result

def Calculate_Hash(text):
    q = 2147483647
    return Gorner_scheme(text) % q


def Search_text(text, sub_text):
    base = 31
    q = 2147483647
    sub_hash = Calculate_Hash(sub_text)
    m = len(sub_text)
    current_hash = Calculate_Hash(text[:m])
    i = 0

    while True:
        if sub_hash == current_hash:
            if sub_text == text[i:i+m]:
                return i
            if i + m >= len(text):
                break

        current_hash = ((current_hash - ord(text[i]) * base ** (m-1)) * base + ord(text[i+m])) % q
        i += 1

    return None


sample_text = "Awersome apple"
sample_search = "some"
print(Search_text(sample_text, sample_search))