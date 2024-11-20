#YOUR CODE FOR EX_0 ADVANCED HERE
DNA_sequence= input('Enter the DNA sequence:')
valid_nucleotides = {'A', 'T', 'G', 'C'}
is_valid_dna = all(nucleotide in valid_nucleotides for nucleotide in DNA_sequence)
if is_valid_dna:
    print(f"Length of the DNA sequence: {len(DNA_sequence)}")

    a_count= DNA_sequence.count('A')
    t_count= DNA_sequence.count('T')
    g_count= DNA_sequence.count('G')
    c_count= DNA_sequence.count('C')
    GC_content_count= DNA_sequence.count('GC')
    print(f"A: {a_count}, T: {t_count}, G: {g_count},C: {c_count},GC: {GC_content_count}")
else:
    print("Error: The entered sequence is not a valid DNA sequence.")
