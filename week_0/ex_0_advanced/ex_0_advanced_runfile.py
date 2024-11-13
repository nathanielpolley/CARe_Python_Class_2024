
DNA_sequence = input('Enter DNA sequence: ')
DNA_sequence = DNA_sequence.upper()

adenine_count = DNA_sequence.count('A')
cytosine_count = DNA_sequence.count('C')
guanine_count = DNA_sequence.count('G')
thymine_count = DNA_sequence.count('T')
sequence_length = len(DNA_sequence)

if adenine_count + cytosine_count + guanine_count + thymine_count != sequence_length:
    print('Invalid DNA sequence. It must contain only A, C, G, and T.')
else:
    gc_content = (guanine_count + cytosine_count) / sequence_length * 100

    print(f"Sequence Length: {sequence_length}")
    print(f"A: {adenine_count}, C: {cytosine_count}, G: {guanine_count}, T: {thymine_count}")
    print(f"GC Content: {gc_content:.2f}%")

