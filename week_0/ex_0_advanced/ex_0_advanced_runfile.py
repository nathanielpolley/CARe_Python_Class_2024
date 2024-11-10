#YOUR CODE FOR EX_0 ADVANCED HERE
"""NAME
    DNA sequence analyzer
  Version
    1.0
  AUTHOR
    JOSE EDGAR LEAL RIVERA
  DESCRIPTION
    A, T, G, C, and GC percentage content is calculated from a DNA sequence entered by the user.
    It excludes 'non-DNA sequences' from the sequence
  CATEGORY
    Sequence Analyzer
  USAGE
    It counts A,T,G,C and GC content fromm a DNA sequence to calculate its percentage
  ARGUMENTS
  seq, A, T, C, G, R, Y, per_GC, perGC2
        exclude 'no bases' of strings"""

import re
# Input the sequence and save it into a variable#
print('Welcome')
seq = input('Enter sequence ')
# IgnoreCase due to FASTA format
seq = seq.upper()
# If there is 'u' the sequence is RNA (find a way that it only recognizes ATGCXN-)
if re.search('[^ATCGRY]', seq) :
    print('The entered sequence is not DNA ')

else:
    # count characters 'A'  'T' 'G' 'C' of the string
    A = seq.count('A')
    T = seq.count('T')
    G = seq.count('G')
    C = seq.count('C')
    R = seq.count('R')
    Y = seq.count('Y')
    # GC percentage


    perGC = ((G + C ) / len(seq)) * 100
    if (R + Y == 0):
     print('Your sequence has', A, 'Adenines,', T, 'Timines,', G, 'Guanines,', C, 'Citocines, and', perGC,
           '% of GC content')

    else:
        perGC2 = ((G + C + R + Y) / len(seq)) * 100

        # print solicited
        print('Your sequence has', A, ' Adenines', T, 'Timines,', G, 'Guanines,', C, 'Citocines,', R+A+G, 'Purines', Y+T+C, 'Pyrimidines and', perGC,'% -', perGC2, '% of GC content')
