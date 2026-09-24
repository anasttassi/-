codon_table = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}

def read_rna(filename):
    with open(filename, "r") as f:
        rna = f.readline().strip()

    return rna

def translate(rna):
    protein = ""  # сюда будем накапливать буквы аминокислот

    # идём по строке rna шагами по 3 символа
    for i in range(0, len(rna), 3):
        codon = rna[i:i + 3]  # берём очередной кодон - кусочек из 3 букв
        amino_acid = codon_table[codon]  # находим аминокислоту по таблице

        if amino_acid == "Stop":
            # встретили стоп-кодон - дальше не читаем и не добавляем его в белок
            break

        protein = protein + amino_acid

    return protein

file_name = "z6"
rna = read_rna(file_name)

result = translate(rna)
print(result)