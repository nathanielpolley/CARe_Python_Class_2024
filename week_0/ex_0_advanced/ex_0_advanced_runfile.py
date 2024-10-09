#YOUR CODE FOR EX_0 ADVANCED HERE

def sequence_input():
    allowed_char = 'A', 'T', 'G', 'C'
    while True:
        sequence = input("Enter the DNA sequence: ").upper()
        if all(char in allowed_char for char in sequence):
            seq_list = list(sequence)
            print("The length of the DNA sequence is", len(seq_list), "bp")
            print("There are ",seq_list.count("A"),"Adenine bases")
            print("There are",seq_list.count("T"), "Thymine bases")
            print("There are",seq_list.count("G"), "Guanine bases")
            print("There are",seq_list.count("C"), "Cytosine bases")
            print("The GC content is",seq_list.count("G")/seq_list.count("C"))
            break
        else:
            print("As far as I know, DNA is made up of 'A','T','G', and 'C' only")
sequence_input()