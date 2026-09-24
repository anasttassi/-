def read_input(filename):
    with open(filename, "r") as f:
        line = f.readline()  

    numbers = line.strip().split()  
    k = int(numbers[0])
    m = int(numbers[1])
    n = int(numbers[2])

    return k, m, n

def probability_dominant(k, m, n):
    total = k + m + n  
    p_nn_nn = (n / total) * ((n - 1) / (total - 1))
   
    p_mm_mm = (m / total) * ((m - 1) / (total - 1))

    p_nn_mm = 2 * (n / total) * (m / (total - 1))
   
    # aa + aa -> 100% 
    # Aa + Aa -> 25% 
    # aa + Aa -> 50% 

    p_recessive = p_nn_nn * 1 + p_mm_mm * 0.25 + p_nn_mm * 0.5

    return 1 - p_recessive

file_name = "z3"
k, m, n = read_input(file_name)

result = probability_dominant(k, m, n)
print(f"{result:.5f}")