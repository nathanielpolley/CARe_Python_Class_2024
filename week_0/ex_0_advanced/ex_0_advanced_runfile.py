def analyze_dna_sequence(dna_sequence):
    sequence_length = len(dna_sequence)

    count_a = dna_sequence.count('A')
    count_c = dna_sequence.count('C')
    count_g = dna_sequence.count('G')
    count_t = dna_sequence.count('T')

    gc_content = (count_g + count_c) / sequence_length * 100 if sequence_length > 0 else 0

    return sequence_length, count_a, count_c, count_g, count_t, gc_content


def main():
    dna_sequence = input("Enter a DNA sequence: ").upper()  # Convert to uppercase for uniformity

    valid_bases = {'A', 'C', 'G', 'T'}

    if not all(base in valid_bases for base in dna_sequence):
        print("Invalid DNA sequence. Please use only the characters A, C, G, and T.")
        return

    length, count_a, count_c, count_g, count_t, gc_content = analyze_dna_sequence(dna_sequence)

    print(f"Sequence Length: {length}")
    print(f"Adenine (A): {count_a}")
    print(f"Cytosine (C): {count_c}")
    print(f"Guanine (G): {count_g}")
    print(f"Thymine (T): {count_t}")
    print(f"GC Content: {gc_content:.2f}%")


if __name__ == "__main__":
    main()
