#YOUR CODE FOR EX_0 INTERMEDIATE HERE
# Input from the user
import math

initial_count = int(input("Enter initial count: "))

# Conditional statements
if initial_count < 1:
    print("invalid initial count")

# Again for final count
final_count = int(input("Enter final count: "))

if initial_count<1 or final_count < initial_count:
    print("invalid final count")

else:
    calculus=math.log(final_count) - math.log(initial_count)
    print(f"Growth rate is: {calculus}")