def is_valid_dna ( sequence ) :
    "Check if the DNA sequence is valid  ( only when it contains A, C, G, T )."
    valid_bases = { 'A', 'C', 'G' , 'T'}
    return all( base in valid_bases for base in sequence.upper())
def analyze_dna ( sequence) :
    "Analyze the DNA and calculate metrics."
    length = len ( sequence)
    adenine_count = sequence.upper().count ('A')
    cytosine_count = sequence.upper().count ('C')
    guanine_count = sequence.upper().count ( 'G')
    thymine_count = sequence.upper().count ('T')

    gc_content = (cytosine_count +guanine_count) / length * 100

    return length, adenine_count, cytosine_count, guanine_count, thymine_count, gc_content

def main():
    dna_sequence = input ("Enter your DNA sequence:"). strip()
    if not is_valid_dna (dna_sequence):
        print ( " invalid Dna sequence, you have to use only A, C, G, T.")
        return

        length, A, C, G, T, gc_content = anamyze_dna (dna_sequence)
        print(f"sequence Lenght: {length}")
        print(f"Adenine (A) : {A}")
        print(f"Cytosine (C) : {C}")
        print(f"Guanine (G) :{G}")
        print(f"Thymine (T) : {T}")
        print(f"GC content : {gc_content:.2f}%")

if __name__== "__main__":
  main()
#


