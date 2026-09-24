# найти расстояние Хэмминга между двумя строками ДНК одинаковой длины
def read_two_strings(filename):
    with open(filename, "r") as f:
        lines = f.readlines()  # читаем все строки файла в список

    # первая строка файла - это s, вторая - это t
    # strip() убирает символ переноса строки \n в конце
    s = lines[0].strip()
    t = lines[1].strip()

    return s, t

def hamming_distance(s, t):
    # проверяем, что строки одинаковой длины, иначе сравнение не имеет смысла
    if len(s) != len(t):
        raise ValueError("строки должны быть одинаковой длины")

    distance = 0
    for i in range(len(s)):
        # сравниваем символы на одинаковой позиции i в обеих строках
        if s[i] != t[i]:
            distance = distance + 1

    return distance

# основная часть программы
file_name = "z2"
s, t = read_two_strings(file_name)

result = hamming_distance(s, t)
print(result)