# найти последовательность с максимальным GC содержанием в FASTA файле

def read_fasta(filename):
    # словарь для хранения id: последовательность
    seqs = {}
    id_now = None  # id последовательности, которую сейчас читаем

    with open(filename) as f:
        for line in f:
            line = line.strip()  # убираем \n в конце строки

            if line.startswith(">"):
                id_now = line[1:]  # убираем символ > из начала
                seqs[id_now] = ""
            else:
                # это часть последовательности, дописываем её к предыдущей
                # (в FASTA последовательность может идти в несколько строк)
                seqs[id_now] = seqs[id_now] + line

    return seqs

def gc_content(seq):
    gc = 0
    for letter in seq:
        if letter == "G" or letter == "C":
            gc = gc + 1

    result = gc / len(seq) * 100
    return result

file_name = "/home/cun/dzinf/file1.txt"
all_seqs = read_fasta(file_name)

max_id = None
max_gc = -1

for seq_id in all_seqs:
    current_seq = all_seqs[seq_id]
    current_gc = gc_content(current_seq)

    if current_gc > max_gc:
        max_gc = current_gc
        max_id = seq_id

print(max_id)
print(f"{max_gc:.6f}")