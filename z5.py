# слить два уже отсортированных массива в один отсортированный массиd алгоритмом слияния

def read_two_arrays(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    # lines[0] - это n (длина A), строку надо пропустить
    # lines[1] - сам массив A
    a_numbers = lines[1].strip().split()
    array_a = [int(x) for x in a_numbers]

    # lines[2] - это m (длина B), тоже просто пропускаем
    # lines[3] - сам массив B
    b_numbers = lines[3].strip().split()
    array_b = [int(x) for x in b_numbers]

    return array_a, array_b

def merge_sorted_arrays(a, b):
    result = []
    i = 0  # указатель на текущую позицию в массиве a
    j = 0  # указатель на текущую позицию в массиве b

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i = i + 1
        else:
            result.append(b[j])
            j = j + 1

    while i < len(a):
        result.append(a[i])
        i = i + 1

    while j < len(b):
        result.append(b[j])
        j = j + 1

    return result

file_name = "z5"
array_a, array_b = read_two_arrays(file_name)

merged = merge_sorted_arrays(array_a, array_b)

merged_str = [str(x) for x in merged]
print(" ".join(merged_str))