#YOUR CODE FOR EX_0 INTERMEDIATE HERE
# Input from the user
import math

time = int(input("Enter time in hours: "))

# Conditional statements
if time < 0:
    print("invalid time")
else:
    initial_count = int(input("Enter initial count: "))

# Conditional statements
if initial_count < 1:
    print("invalid initial count")

# Again for final count
final_count = int(input("Enter final count: "))

if initial_count<1 or final_count < initial_count:
    print("invalid final count")

else:
    calculus=(math.log(final_count) - math.log(initial_count)) / time
    print(f"Growth rate is: {calculus}")