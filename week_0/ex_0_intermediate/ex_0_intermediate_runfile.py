#YOUR CODE FOR EX_0 INTERMEDIATE HERE
import math
try:
  final_count=int(input("put the final count of the microbes:"))
except ValueError:
    print("kindly enter number")
try:
    initial_count=int(input("put the initial count of microbes:"))
except ValueError:
    print("kindly enter a number")
try:
    time=int(input("put the time in days:"))
except ValueError:
    print("kindly enter a number")

if initial_count  <=0 or final_count<= 0 or time <= 0:
    print( "initial, final counts and time should be positive")

elif final_count<= initial_count :
    print("The final count must be greater than the initial one")
else:
    growth_rate=(math.log(final_count)-math.log(initial_count)) /time
    print(f"the growth_rate is :{growth_rate=} per day")
