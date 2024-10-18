#YOUR CODE FOR EX_0 INTERMEDIATE HERE

"""NAME
    Microbial Growth Rate Calculator
  Version
    1.0
  AUTHOR
    JOSE EDGAR LEAL RIVERA
  DESCRIPTION
    Calculate and display the growth rate using the formula: Growth Rate = (ln(final count) - ln(initial count)) / time.
  CATEGORY
    Calculator
  USAGE
    It calculates Growth rate given an initial cell count, a final cell count and time elapsed
  ARGUMENTS
  i_c, i_f, t, GR
        exclude invalid numbers """

import re
import math
# Input into a variable#
print('Welcome')
i_c = (input('Enter initial cell counts: '))
f_c = (input('Enter final cell counts: '))
t = (input('Enter time elapsed: '))
#Check it is a digit and handle error
pattern = '[\\d]+'
m1 = re.match(pattern, i_c)
m2 = re.match(pattern, f_c)
m3 = re.match(pattern, t)
if (m1 is None)|(m2 is None)|(m3 is None):
    print('The input is not a valid number ')
else:
    #Calculate GR
    GR = (math.log(int(f_c)) - math.log(int(i_c))) / int(t)

    print('The Microbial Growth Rate of your data is', GR,)

