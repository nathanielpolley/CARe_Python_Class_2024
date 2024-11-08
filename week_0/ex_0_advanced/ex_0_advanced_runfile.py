DNA_sequence = input("Enter DNA sequence: ")
DNA_length = len(DNA_sequence)
print(DNA_length)
count_A= DNA_sequence.count("A")
print("count a", count_A)
count_T= DNA_sequence.count("T")
print("count t", count_T)
count_C= DNA_sequence.count("C")
print("count c", count_C)
count_G= DNA_sequence.count("G")
print("count G", count_G)


if (count_C+count_G+count_T+count_A ) != DNA_length:
     DNA_sequence= (input(" invalid, reenter a new DNA sequence: "))

print((count_C + count_G) / DNA_length * 100)


