def can_color(v, colors, k, adj):
    if v == len(adj):
        return True
    for c in range(1, k + 1):
        conflict = False
        for u in range(len(adj)):
            if adj[v][u] and colors[u] == c:
                conflict = True
                break
        if not conflict:
            colors[v] = c
            if can_color(v + 1, colors, k, adj):
                return True
            colors[v] = 0
    return False


def min_colors(adj):
    N = len(adj)
    for k in range(1, N + 1):
        colors = [0] * N
        if can_color(0, colors, k, adj):
            return k, colors
    return N, [0] * N


# ---------- Создаём граф из видео ----------
N = 10
adj = [[False] * N for _ in range(N)]

# Рёбра, восстановленные по объяснению спикера
edges = [
    (3, 4), (3, 1), (3, 2), (3, 6),   # D-E, D-B, D-C, D-G
    (1, 0), (1, 2), (1, 7),           # B-A, B-C, B-H
    (2, 0), (2, 5), (2, 7),           # C-A, C-F, C-H
    (4, 5), (4, 6),                   # E-F, E-G
    (5, 7),                           # F-H
    (6, 8),                           # G-I
    (7, 9),                           # H-J
    (8, 9)                            # I-J
]

for u, v in edges:
    adj[u][v] = True
    adj[v][u] = True

# -----------------------------------------

# Ищем минимальную раскраску
min_k, coloring = min_colors(adj)

color_names = {1: 'синий', 2: 'зелёный', 3: 'красный'}

print(f"Минимальное количество цветов: {min_k}")
print("Раскраска вершин:")
names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
for i, name in enumerate(names):
    print(f"  {name}: цвет {color_names[coloring[i]]}")