#YOUR CODE FOR EX_0 ADVANCED HEREfrom logging import exception
from logging import exception

DNA_sequence= input("enter DNA sequence")
# OUR CODE FOR EX_0 ADVANCED HERE

sequence_length = len(DNA_sequence)

print(f"The length of the DNA sequence is {sequence_length}")
print(f'The number of adenine is : {DNA_sequence.count("A")}')
print(f'The number of cytosine is : {DNA_sequence.count("C")}')
print(f'The number of guanine is : {DNA_sequence.count("G")}')
print(f'The number of thymine is : {DNA_sequence.count("T")}')
print(f'The number of GC is : {DNA_sequence.count("GC")}')

if DNA_sequence.count("A") + DNA_sequence.count("C") + DNA_sequence.count("G") + DNA_sequence.count("T") != sequence_length:
    exception("the input is not a valid DNA sequence")