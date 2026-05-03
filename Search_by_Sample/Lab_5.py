def get_max_prefix(text,lower_index, higher_index):
  result = 0
  while higher_index < len(text):
    if text[lower_index]!=text[higher_index]:
      break
    result += 1
    lower_index += 1
    higher_index += 1
  return result

def z_function(text):
  pref = [0 for _ in range(len(text))]
  pref[0] = len(text)
  start, end = 0, 0
  for i in range(1, len(text)):
    if i < end:
      if i + pref[i-start] < end:
        pref[i] = pref[i-start]
      else:
        pref[i] = end - i + get_max_prefix(text,end-i,end)
        if i+pref[i] > end:
          start, end = i, i+pref[i]
    else:
      pref[i] = get_max_prefix(text,0,i)
      start, end = i, i+pref[i]
  return pref



def get_suffix_table(text):
  return z_function(text[::-1])[::-1]

def get_good_suffix(text):
  m = len(text)
  suf_table = get_suffix_table(text)
  good_suf_table = [0 for _ in range(m)]
  for j in range(m-1):
    i = m - suf_table[j] - 1
    good_suf_table[i] = m-1-j
  if good_suf_table[m-1] == 0:
    good_suf_table[m-1] = m
  j = m - 1
  part = 0
  for i in range(m-1):
    if good_suf_table[i] == 0:
      if j > m - 2 - i:
        for j in range(m-2-i,-1,-1):
          if suf_table[j] == j + 1:
            part = suf_table[j]
            break
        else:
          part = 0
      good_suf_table[i] = m - part
  return good_suf_table


def get_bed_char(text):
    bed_char = {}
    for i,ch in enumerate(text[:-1]):
        bed_char[ch] = i
    return bed_char



def search_boyer_moore(text, pat):
    good_suffics_table = get_good_suffix(pat)
    bed_char = get_bed_char(pat)
    m = len(pat)
    i = m - 1
    while i < len(text):
        k = i
        for j in range(m-1,-2,-1):
            if j == -1:
                return i - m + 1
            if pat[j] != text[k]:
                delta_1 = j - bed_char.get(text[k], 0)
                if delta_1 <=0:
                    delta_1 = 1
                delta_2 = good_suffics_table[j]
                i += max(delta_1, delta_2)
                break
            k -=1
    return None
            



pat = "ATCAT"
text = "TGCTATAAATCATCTCTAACGCT "

print(search_boyer_moore(text, pat))
print(text[search_boyer_moore(text, pat):])
