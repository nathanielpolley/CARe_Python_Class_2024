def calculate_seq (seq):
    A = seq.count('A')
    C = seq.count('C')
    T = seq.count('T')
    G = seq.count('G')
    gc_content = round(((G + C) / len(seq)) * 100, 2)
    print(f'Your DNA sequence has:\n {A} Adenines\n {C} Cytosines\n {G} Guanines\n {T} Thymines\n {gc_content} GC content')


def user_seq():
    Nucleotides_list = ['A', 'C', 'G', 'T']
    while True:
        seq = input('Enter your sequence: ').upper()
        if all(nuc in Nucleotides_list for nuc in seq):
            calculate_seq(seq)
            break
        else:
            print('Invalid input. Please enter a valid DNA sequence.')

user_seq()