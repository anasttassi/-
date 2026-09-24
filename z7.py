# для каждой вершины графа найти сумму степеней ее соседей

def read_graph(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    # первая строка содержит n (число вершин) и m (число ребер)
    first_line = lines[0].strip().split()
    n = int(first_line[0])
    m = int(first_line[1])

    # словарь: вершина -> список её соседей
    # сразу создаем запись для каждой вершины от 1 до n с пустым списком соседей
    neighbors = {}
    for vertex in range(1, n + 1):
        neighbors[vertex] = []

    # читаем m строк с ребрами, начиная со второй строки файла (индекс 1)
    for i in range(1, m + 1):
        edge = lines[i].strip().split()
        v1 = int(edge[0])
        v2 = int(edge[1])

        neighbors[v1].append(v2)
        neighbors[v2].append(v1)

    return n, neighbors

def compute_degrees(neighbors, n):
    degrees = {}
    for vertex in range(1, n + 1):
        degrees[vertex] = len(neighbors[vertex])

    return degrees

def compute_double_degree(neighbors, degrees, n):
    result = []

    for vertex in range(1, n + 1):
        total = 0
        for neighbor in neighbors[vertex]:
            total = total + degrees[neighbor]

        result.append(total)

    return result

file_name = "z7"
n, neighbors = read_graph(file_name)

degrees = compute_degrees(neighbors, n)
answer = compute_double_degree(neighbors, degrees, n)

answer_str = [str(x) for x in answer]
print(" ".join(answer_str))