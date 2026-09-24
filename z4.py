# для каждого из k массивов длины n найти элемент,который встречается строго больше n/2 раз, или вывести -1, если такого нет

def read_arrays(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    first_line = lines[0].strip().split()
    k = int(first_line[0])
    n = int(first_line[1])

    arrays = [] 
    for i in range(1, k + 1):
        numbers = lines[i].strip().split()
        array = [int(x) for x in numbers]
        arrays.append(array)

    return n, arrays

def find_majority(array, n):
    counts = {} 

    for number in array:
        if number in counts:
            counts[number] = counts[number] + 1
        else:
            counts[number] = 1

    for number in counts:
        if counts[number] > n / 2:
            return number

file_name = "z4"
n, arrays = read_arrays(file_name)

answers = []
for array in arrays:
    result = find_majority(array, n)
    answers.append(str(result)) 

print(" ".join(answers))