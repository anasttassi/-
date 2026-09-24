# найти расстояние Хэмминга между двумя строками ДНК одинаковой длины
def read_two_strings(filename):
    with open(filename, "r") as f:
        lines = f.readlines()  

    s = lines[0].strip()
    t = lines[1].strip()

    return s, t

def hamming_distance(s, t):
    if len(s) != len(t):
        raise ValueError("строки должны быть одинаковой длины")

    distance = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            distance = distance + 1

    return distance

file_name = "z2"
s, t = read_two_strings(file_name)

result = hamming_distance(s, t)
print(result)