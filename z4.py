# для каждого из k массивов длины n найти элемент,который встречается строго больше n/2 раз, или вывести -1, если такого нет

def read_arrays(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    # первая строка содержит два числа: k и n
    first_line = lines[0].strip().split()
    k = int(first_line[0])
    n = int(first_line[1])

    arrays = []  # тут будем хранить все k массивов
    for i in range(1, k + 1):
        # строки с массивами идут начиная со второй строки файла (индекс 1)
        numbers = lines[i].strip().split()
        array = [int(x) for x in numbers]  # превращаем каждую строку-число в int
        arrays.append(array)

    return n, arrays

def find_majority(array, n):
    counts = {}  # словарь: число -> сколько раз оно встретилось

    for number in array:
        if number in counts:
            counts[number] = counts[number] + 1
        else:
            counts[number] = 1

    # теперь ищем число, которое встретилось строго больше n/2 раз
    for number in counts:
        if counts[number] > n / 2:
            return number

    # если цикл закончился и мы ничего не вернули - мажоритарного элемента нет
    return -1

file_name = "z4"
n, arrays = read_arrays(file_name)

answers = []
for array in arrays:
    result = find_majority(array, n)
    answers.append(str(result))  # переводим число в строку, чтобы потом склеить через пробел

print(" ".join(answers))