#YOUR CODE FOR EX_0 ADVANCED HERE
"""NAME
    DNA sequence analyzer
  Version
    1.0
  AUTHOR
    JOSE EDGAR LEAL RIVERA
  DESCRIPTION
    An AT content percentage is calculated form a DNA sequence entered by the user.
    It excludes 'u' from the sequence and recognizes it is not DNA
  CATEGORY
    Sequence Analyzer
  USAGE
    It counts A,T,G,C and GC content fromm a DNA sequence to calculate its percentage
  ARGUMENTS
  seq, A, T, C, G, per_GC
        exclude 'no bases' of strings"""

import re
# Input the sequence and save it into a variable#
print('Welcome')
seq = input('Enter sequence ')
# IgnoreCase due to FASTA format
seq = seq.upper()
# If there is 'u' the sequence is RNA (find a way that it only recognizes ATGCXN-)
if re.search('[^ATCG]', seq) :
    print('The entered sequence is not DNA ')
else:
    # count characters 'A'  'T' 'G' 'C' of the string
    A = seq.count('A')
    T = seq.count('T')
    G = seq.count('G')
    C = seq.count('C')
    # GC percentage
    perGC = ((G + C) / len(seq)) * 100
    # print solicited
    print('Your sequence has', A, 'of Adenine,', T, 'of Timine,', G, 'of Guanine,', C, 'of Citocine, and', perGC, '% of GC content')
