def analyze_dna_sequence(dna_sequence):
    # Initialize counts
    a_count = dna_sequence.count('A')
    c_count = dna_sequence.count('C')
    g_count = dna_sequence.count('G')
    t_count = dna_sequence.count('T')

    # Calculate total length and GC content
    sequence_length = len(dna_sequence)
    gc_content = (g_count + c_count) / sequence_length * 100 if sequence_length > 0 else 0

    # Display results
    print(f"Sequence Length: {sequence_length}")
    print(f"Adenine (A) Count: {a_count}")
    print(f"Cytosine (C) Count: {c_count}")
    print(f"Guanine (G) Count: {g_count}")
    print(f"Thymine (T) Count: {t_count}")
    print(f"GC Content: {gc_content:.2f}%")


def main():
    # Prompt user for input
    dna_sequence = input("Enter a DNA sequence (A, C, G, T): ").upper()

    # Validate the input
    if all(base in 'ACGT' for base in dna_sequence):
        analyze_dna_sequence(dna_sequence)
    else:
        print("Error: Invalid DNA sequence. Please use only A, C, G, and T.")


if __name__ == "__main__":
    main()